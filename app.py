from flask import Flask, jsonify,request
from src.databaseConnect import query_cosmos_db
from src.embedding import get_embedding_model
from src.getVectorStore import get_vector_store
from src.translate import translate
from src.searchVectorDb import search_vector_db
from ollama import Client
from langchain_community.chat_models import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers.string import StrOutputParser
from langchain_core.runnables.passthrough import RunnablePassthrough


import json
import os


os.environ["AZURESEARCH_FIELDS_ID"] = "id"
# os.environ["AZURESEARCH_FIELDS_CONTENT"] = "chunk"
os.environ["AZURESEARCH_FIELDS_CONTENT_VECTOR"] = "content_vector"
# os.environ["AZURESEARCH_FIELDS_TAG"] = "metadata"
llm = ChatOllama(model = 'phi3')



client = Client(host='http://localhost:11434')
embeddings = get_embedding_model()
vector_store = get_vector_store(embeddings)
retriever = vector_store.as_retriever()
# add_data_to_vector_db(embeddings, vector_store)

app = Flask(__name__)




# Fetch all data from vector db
@app.route('/fetch_all_data',methods=['GET'])
def get_data():
    database_name = 'Test1'
    container_name = 'DATA'
    query_text = f"SELECT * FROM Items"
    items = query_cosmos_db(database_name, container_name,query_text)
    return jsonify(items)


# Fetch data from noSql db which matches the query completely
# {
#     "value":"SG02 \"++ST100+SD002\":Schutztuer entriegelt"
# }
@app.route('/fetch_data',methods=['GET'])
def get_db_data():
    data = json.loads(request.data)
    value = data.get("value")
    database_name = 'Test1'
    container_name = 'DATA'
    valuetext = request.args.get('valuetext', default=value, type=str)
    query_text = f"SELECT * FROM Items WHERE Items.valuetext = '{valuetext}'"
    items = query_cosmos_db(database_name, container_name, query_text)
    return jsonify(items)

# Fetch data from vector db
@app.route('/free_text_search',methods=['GET'])
def get_vector_data():
    data = json.loads(request.data)
    value = data.get("value")
    summary = data.get("summary")
    translatedValue = translate([value])[0]['translations'][0]['text']

    results = search_vector_db(translatedValue,vector_store)
    response = {
        "results":results
    }

    if summary:

        # Template for generating the answer based on context and question
        prompt_text = """Answer the question based only on the following context in shortened bullet points:
            {context}
            Question: {question}
            """
        # Create a prompt using the template
        prompt_template = ChatPromptTemplate.from_template(prompt_text)

        # Chain of operations for RAG
        chain = (
                {"context": retriever, "question": RunnablePassthrough()}  # Pass context and question
                | prompt_template  # Use the prompt template
                | llm  # Apply the local model
                | StrOutputParser()  # Parse the output to a string
        )

        res = chain.invoke(translatedValue)  # Invoke the RAG chain with the user's question
        response['summary'] = res

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
