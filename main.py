import warnings
import os
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader
from langchain_community.vectorstores import Qdrant
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Suppress warnings
warnings.filterwarnings("ignore")

# Initialize the embeddings model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/paraphrase-MiniLM-L6-v2"
)

# Load the documents from the 'data' folder
loader = DirectoryLoader('data/', glob="**/*.md", show_progress=True)
documents = loader.load()

# Split the documents into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=40)
docs = text_splitter.split_documents(documents)

# Create the Qdrant index (in-memory)
qdrant = Qdrant.from_documents(
    docs,
    embeddings,
    location=":memory:",
    collection_name="test",
    show_progress=True
)

# Function to process a query and return the most relevant document
def process_query(query: str):
    found_docs = qdrant.similarity_search_with_score(query)
    documents, score = found_docs[0]
    return documents.page_content, score

if __name__ == "__main__":
    # Simple test
    query = "Tell me how to connect to qdrant_client"
    result, score = process_query(query)
    print(f"Result: {result}")
    print(f"Score: {score}")
