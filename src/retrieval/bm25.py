from rank_bm25 import BM25Okapi
from pathlib import Path
import joblib

#bm25 keyword search implementation for document retrieval

bm25 = None
documents = []
metadata = []

INDEX_FILE = Path("data/indexes/bm25.pkl")

class BM25Searcher:

    def __init__(self, chunks=None):

        # if chunks is not None:
        #     build_bm25(chunks)
        load_bm25()
        
     # Search for documents using BM25 keyword search
    def search(self, query, k=10):

        return bm25_search(query, k=k)

def build_bm25(chunks):

    global bm25
    global documents
    global metadata

    documents = [c.page_content for c in chunks]
    metadata = [c.metadata for c in chunks]

    tokenized = [doc.lower().split() for doc in documents]

    bm25 = BM25Okapi(tokenized)
    print(f"BM25 indexed {len(documents)} chunks.")
    INDEX_FILE.parent.mkdir(parents=True, exist_ok=True)

    joblib.dump(
        {
            "bm25": bm25,
            "documents": documents,
            "metadata": metadata
        },
        INDEX_FILE
    )

    print(f"Saved BM25 index to {INDEX_FILE}")
    
def load_bm25():

    global bm25
    global documents
    global metadata

    if not INDEX_FILE.exists():
        raise FileNotFoundError(
            "BM25 index not found. Run ingestion first."
        )

    data = joblib.load(INDEX_FILE)

    bm25 = data["bm25"]
    documents = data["documents"]
    metadata = data["metadata"]

    print(
        f"Loaded BM25 index ({len(documents)} chunks)"
    )
    
    
def bm25_search(query, k=10):
    if bm25 is None:
        raise RuntimeError(
            "BM25 index has not been built."
        )

    tokens = query.lower().split()

    scores = bm25.get_scores(tokens)

    ranked = sorted(
        enumerate(scores),
        key=lambda x: x[1],
        reverse=True
    )[:k]
    
    results = []
    
    for index, score in ranked:

        results.append(
            {
                "document": documents[index],
                "metadata": metadata[index],
                "score": float(score),
                "source": "bm25"
            }
        )

    return results