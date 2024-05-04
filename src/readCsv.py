import os
os.environ["AZURESEARCH_FIELDS_ID"] = "id"
# os.environ["AZURESEARCH_FIELDS_CONTENT"] = "chunk"
os.environ["AZURESEARCH_FIELDS_CONTENT_VECTOR"] = "content_vector"
# os.environ["AZURESEARCH_FIELDS_TAG"] = "metadata"


from langchain.schema.document import Document
import pandas as pd

def read_csv(file_path="/content/plc_merge_data.csv"):
    df = pd.read_csv(file_path)
    # docs = [Document(text=formatted_content)]
    data = df[['notificationNumber','Solution']]

    docs = [Document(page_content=x[1]['Solution']) for x in df.iterrows()]
    return data