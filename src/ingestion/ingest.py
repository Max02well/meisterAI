#This page loads documents, chunks them, and adds them to the ChromaDB collection.
# It is to be run once to populate the database.
import uuid

from src.ingestion.loader import load_documents
from src.ingestion.chunker import chunk_documents
from src.ingestion.embedder import get_collection


documents = load_documents()

chunks = chunk_documents(documents)
if not chunks:
    print("No chunks were created. Please check the documents and try again.")
    exit()

collection = get_collection()

collection.add(

    ids=[str(uuid.uuid4()) for _ in chunks],

    documents=[
        chunk.page_content
        for chunk in chunks
    ],

    metadatas=[
        chunk.metadata
        for chunk in chunks
    ]
)

print("Finished ingesting.")