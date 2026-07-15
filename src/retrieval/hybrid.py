#merge vector search and bm25 keyword search for document retrieval
from src.retrieval.vector_search import VectorSearcher
from src.retrieval.bm25 import BM25Searcher, build_bm25
from src.ingestion.chunker import chunk_documents
from src.ingestion.loader import load_documents

class HybridSearcher:

    def __init__(self):

        self.vector = VectorSearcher()
        # documents = load_documents()
        # chunks = chunk_documents(documents)
        self.keyword = BM25Searcher()
        
     # Search for documents using both vector and keyword search, then merge results   
    def search(self, query):

        vector_results = self.vector.search(query, k=8)

        keyword_results = self.keyword.search(query, k=8)

        return self.merge(
            vector_results,
            keyword_results
        )
        
    # Merge vector and keyword results, removing duplicates based on manual and page metadata
    # LATER replace THIS with Reciprocal Rank Fusion.
    def merge(
        self,
        vector_results,
        keyword_results
    ):

        merged = []

        seen = set()

        #
        # First keep vector results
        #

        for doc, meta, distance in zip(

            vector_results["documents"][0],

            vector_results["metadatas"][0],

            vector_results["distances"][0]

        ):

            key = (
                meta["manual"],
                meta["page"]
            )

            if key not in seen:

                merged.append({

                    "document": doc,

                    "metadata": meta,

                    "distance": distance,

                    "source": "vector"

                })

                seen.add(key)

        #
        # Add BM25 documents not already present
        #

        for result in keyword_results:

            key = (
                result["metadata"]["manual"],
                result["metadata"]["page"]
            )

            if key not in seen:

                merged.append(result)

                seen.add(key)

        return merged