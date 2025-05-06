from RAG_operations import load_documents, chunk_documents, setup_chroma_db, retrieve_context, generate_response, display_results

def access_world_info(search_prompt):
    # Set embedding and LLM models
    embedding_model = "nomic-embed-text"  # Change to your preferred embedding model
    llm_model = "llama3.2:latest"  # Change to your preferred LLM model
    
    # 1. Load documents
    data_dir = "project/data"
    documents = load_documents(data_dir)
    
    # 2. Chunk documents using ChromaDB chunker
    chunks = chunk_documents(documents)
    
    # 3. Set up ChromaDB with Ollama embeddings
    collection = setup_chroma_db(
        chunks, 
        ollama_model=embedding_model
    )
    # 4. Example queries
    query = search_prompt
    
    # Retrieve context
    contexts = retrieve_context(collection, query)
    
    # Generate response
    response = generate_response(query, contexts, model=llm_model)
    
    # Display results
    #display_results(query, contexts, response)

    return(response)