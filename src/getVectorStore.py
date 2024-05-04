import os
os.environ["AZURESEARCH_FIELDS_ID"] = "id"
# os.environ["AZURESEARCH_FIELDS_CONTENT"] = "chunk"
os.environ["AZURESEARCH_FIELDS_CONTENT_VECTOR"] = "content_vector"
# os.environ["AZURESEARCH_FIELDS_TAG"] = "metadata"

from langchain_community.vectorstores.azuresearch import AzureSearch
from azure.search.documents.indexes.models import (
    SearchableField,
    SearchField,
    SearchFieldDataType
)

def get_vector_store(embeddings):
    vector_store_address: str = "https://bmw-hack-10.search.windows.net"
    vector_store_password: str = "bsVLrllnrwzoAzPbMDutfbBMUXJk8e2ctZ3ksBxFCaAzSeDEvkZV"
    index_name: str = "langchain-vector-demo"
    index_name: str = "langchain-vector-demo-custom"

    fields = [
        SearchableField(name="id", type=SearchFieldDataType.String, key=True),
        SearchableField(
            name="content",
            type=SearchFieldDataType.String,
            searchable=True,
        ),
        SearchField(name="content_vector", type=SearchFieldDataType.Collection(SearchFieldDataType.Single),
                    searchable=True, vector_search_dimensions=1536, vector_search_profile_name="myHnswProfile",),
        SearchableField(
            name="metadata",
            type=SearchFieldDataType.String,
            searchable=True,
        ),
    ]


    vector_store: AzureSearch = AzureSearch(
        azure_search_endpoint=vector_store_address,
        azure_search_key=vector_store_password,
        index_name=index_name,
        embedding_function=embeddings.embed_query,
        fields=fields,
    )

    return vector_store