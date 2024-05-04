from readCsv import read_csv
from translate import translate

def add_data_to_vector_db(embeddings, vector_store):
    df = read_csv("/content/plc_merge_data.csv")
    n = 10
    texts = [x[1]['Solution'] for x in df.iterrows()][:n]
    texts = [x['translations'][0]['text'] for x in translate(texts)]
    metadata = [{"id":str(x[1]['notificationNumber'])} for x in df.iterrows()][:n]

    vector_store.add_texts(texts, metadata)