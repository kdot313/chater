from langchain_astradb import AstraDBVectorStore
from dotenv import load_dotenv
import google.generativeai as genai
from langchain.embeddings import HuggingFaceEmbeddings
import os
import pandas as pd
from ecommbot.data_converter import dataconveter

load_dotenv()

ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
ASTRA_DB_KEYSPACE = os.getenv("ASTRA_DB_KEYSPACE")
HF_TOKEN = os.getenv("HF_TOKEN")

# Create embeddings object using an open-source model
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")

def ingestdata(status):
    vstore = AstraDBVectorStore(
            embedding=embedding,
            collection_name="chatbotecomm",
            api_endpoint=ASTRA_DB_API_ENDPOINT,
            token=ASTRA_DB_APPLICATION_TOKEN,
            namespace=ASTRA_DB_KEYSPACE,
        )
    
    storage=status
    
    if storage==None:
        docs=dataconveter()
        inserted_ids = vstore.add_documents(docs)
    else:
        return vstore
    return vstore, inserted_ids

if __name__=='__main__':
    vstore,inserted_ids=ingestdata(None)
    print(f"\nInserted {len(inserted_ids)} documents.")
    results = vstore.similarity_search("can you tell me the low budget sound basshead.")
    for res in results:
            print(f"* {res.page_content} [{res.metadata}]")