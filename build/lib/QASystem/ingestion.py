from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_aws.embeddings import BedrockEmbeddings
import boto3

# Initialize Bedrock client
bedrock = boto3.client(service_name="bedrock-runtime")
bedrock_embeddings = BedrockEmbeddings(
    model_id="amazon.titan-embed-text-v2:0",
    client=bedrock
)

def data_ingestion():
    loader = PyPDFDirectoryLoader("./data")
    documents = loader.load()
    if not documents:
        raise ValueError("No documents found in './data'. Check the directory and file permissions.")
    
    print(f"Loaded {len(documents)} documents.")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    docs = text_splitter.split_documents(documents)
    if not docs:
        raise ValueError("Text splitting returned no chunks. Check the text_splitter configuration.")
    
    print(f"Split into {len(docs)} chunks.")
    for i, doc in enumerate(docs):
        print(f"Chunk {i + 1}: {doc.page_content[:100]}...")
    return docs

def get_vector_store(docs):
    valid_docs = []
    valid_embeddings = []
    
    for i, doc in enumerate(docs):
        if not doc.page_content.strip():
            print(f"Skipping empty or whitespace-only chunk {i + 1}.")
            continue
        try:
            print(f"Generating embedding for chunk {i + 1}: {doc.page_content[:50]}...")
            embedding = bedrock_embeddings.embed_text(doc.page_content)
            valid_docs.append(doc)
            valid_embeddings.append(embedding)
        except Exception as e:
            print(f"Error generating embedding for chunk {i + 1}: {e}")
    
    if not valid_embeddings:
        raise ValueError("No embeddings were successfully generated. Check the input documents and Bedrock setup.")
    
    print(f"Generated embeddings for {len(valid_embeddings)} chunks.")
    
    vector_store_faiss = FAISS.from_documents(valid_docs, bedrock_embeddings)
    vector_store_faiss.save_local("faiss_index")
    print("FAISS index saved successfully.")
    return vector_store_faiss

if __name__ == '__main__':
    try:
        docs = data_ingestion()
        get_vector_store(docs)
    except Exception as e:
        print(f"An error occurred: {e}")
