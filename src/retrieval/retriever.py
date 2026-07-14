from chromadb import PersistentClient


class Retriever:

    def __init__(self):
        client = PersistentClient(path="./chroma_db")

        self.collection = client.get_or_create_collection(
            name="knowledge_base"
        )

    def search(self, query: str, k: int = 5):

        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )

        return results