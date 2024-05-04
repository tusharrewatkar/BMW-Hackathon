def search_vector_db(query ,vector_store, k = 3, search_type = "hybrid"):
     # Perform a similarity search
    docs = vector_store.similarity_search(
        query=query,
        k=k,
        search_type=search_type,
        FIELDS_CONTENT_VECTOR = 'translated_text'
    )
    return [{"content":x.page_content, "id":x.metadata['id']} for x in docs]