  
from src.retrieval.hybrid import HybridSearcher
from src.reranking.cross_encoder import Reranker


class Retriever:

    def __init__(self):

        self.searcher = HybridSearcher()
        self.reranker = Reranker()

    def search(self, query):

      results = self.searcher.search(query)
      
      return self.reranker.rerank(
            query,
            results
        )