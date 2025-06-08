from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

def execute():
    documents = SimpleDirectoryReader(input_dir="/Users/aaronseibert/Downloads/paperless_test_sewer_bills/").load_data(num_workers=4)
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine()
    response = query_engine.query("How often are these bills due?")
    return(response)