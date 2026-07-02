import chromadb

#Initialize the ChromaDB Client and create a Collection
# chroma_client = chromadb.Client()
# collection = chroma_client.create_collection(name="test_collection")
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)


#Add documents to the collection with their respective metadata and unique IDs. Each document is tagged with source information in the metadata.
collection.add(
    documents=[
        "This is a document about machine learning",
        "This is another document about data science",
        "A third document about artificial intelligence",
        "This is a deep learning document.",
        "This is the fifth document."
        
    ],
    metadatas=[
        {"source": "test1"},
        {"source": "test2"},
        {"source": "test3"},
        {"source": "test4"},
        {"source": "test5"}
    ],
    ids=[
        "1",
        "2",
        "3",
        "4",
        "5"
    ]
)

results = collection.query(
    query_texts=[
        "What is a document."
    ],
    n_results=3
)

print(results)

for id,doc, meta, distance in zip(
    results["ids"][0],
    results["documents"][0],
    results["metadatas"][0],
    results["distances"][0]
):
    print("=" * 40)
    print("ID :",id)
    print("Document :", doc)
    print("Source   :", meta["source"])
    print("Distance :", distance)