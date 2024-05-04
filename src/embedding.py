from langchain_openai import AzureOpenAIEmbeddings, OpenAIEmbeddings
def get_embedding_model():
    model: str = "text-embedding-ada-002"
    # Option 2: use an Azure OpenAI account with a deployment of an embedding model
    azure_endpoint: str = "https://bmw-hackathon-g10-sn.openai.azure.com/"
    azure_openai_api_key: str = "25567232679340a084327ce0868f4e65"
    azure_openai_api_version: str = "2023-11-01"
    azure_deployment: str = "text-embedding-ada-002"

    embeddings: AzureOpenAIEmbeddings = AzureOpenAIEmbeddings(
    # azure_deployment=azure_deployment,
    openai_api_version="2024-02-01",
    azure_endpoint=azure_endpoint,
    api_key=azure_openai_api_key,
    )

    return embeddings