# cosmos_connection.py

from azure.cosmos import CosmosClient, exceptions, PartitionKey

def query_cosmos_db(database_name, container_name,query_text):
    # Azure Cosmos DB credentials
    url = 'https://bmw-hack-no-sql-g10.documents.azure.com:443/'
    key = 'IIovIt6c17SSAF3WZmKyHxHcqNUf4o5qyCY74QiKLhCFUD1iXqGgA9XB98fPDXW4Q7Y1zWO3X3NiACDbQmgo1Q=='

    # Create a Cosmos client
    client = CosmosClient(url, credential=key)

    # Access the database and container
    database = client.get_database_client(database_name)
    container = database.get_container_client(container_name)

    # Query items in the container
    items = list(container.query_items(query=query_text, enable_cross_partition_query=True))

    # Collect and return items
    return items
