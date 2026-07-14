#CLI to allow users to ask questions and get answers from MeisterAI.

from src.retrieval.retriever import Retriever

retriever = Retriever()

question = input("Ask MeisterAI > ")

results = retriever.search(question)

print("\nTop Results\n")

# for doc, meta, distance in zip(
#     results["documents"][0],
#     results["metadatas"][0],
#     results["distances"][0]
# ):

#     print("=" * 70)

#     # print("Distance :", distance)

#     # print("Source   :", meta["source"])
#     # print("Page:", meta.get("page", "N/A"))
#     print(f"Brand    : {meta['brand']}")
#     print(f"Engine   : {meta['engine']}")
#     print(f"Category : {meta['category']}")
#     print(f"Manual   : {meta['manual']}")
#     print(f"Page     : {meta['page']}")
#     print(f"Distance : {distance:.3f}")
    
#     print("\nDocument")
#     print("-" * 70)

#     print()

#     print(doc[:600])

#     print()

for result in results:

    meta = result["metadata"]

    print("=" * 70)

    print(f"Brand    : {meta['brand']}")
    print(f"Engine   : {meta['engine']}")
    print(f"Category : {meta['category']}")
    print(f"Manual   : {meta['manual']}")
    print(f"Page     : {meta['page']}")

    if "distance" in result:
        print(f"Distance : {result['distance']:.3f}")
        print(f"Score : {result['rerank_score']:.3f}")

    print()

    print(result["document"][:600])

    print()