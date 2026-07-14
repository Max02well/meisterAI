import chromadb


client = chromadb.PersistentClient(path="./chroma_db")


collection = client.get_or_create_collection(
    name="knowledge_base"
)


def get_collection():
    return collection

print("ChromaDB collection initialized and ready for use!")