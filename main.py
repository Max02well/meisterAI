import uvicorn

if __name__ == "__main__":
    uvicorn.run("src.api.api:app", host="0.0.0.0", port=8000, reload=True)


# def main():
#     print("Hello from rag-projects!")


# if __name__ == "__main__":
#     main()

# Metadata Example

# When ingesting documents
# {
#     "brand":"BMW",
#     "model":"F30",
#     "engine":"N47",
#     "year":"2014",
#     "category":"Engine",
#     "chapter":"Timing Chain"
# }

# This allows filtering.

# User asks--># BMW F30 timing chain

# You retrieve only

# brand=BMW

# model=F30

# chapter=Timing Chain

# instead of every BMW document.

# Future AI Features

# Once the text-based RAG is working well, you can expand it significantly:
# VIN-aware retrieval: Decode a VIN, identify the exact model, engine, and year, then automatically filter the knowledge base.
# OBD-II integration: Upload a scan from an OBD reader and have the assistant explain fault codes using the manuals.
# Image-based diagnostics: Upload a photo of an engine bay, dashboard warning light, or damaged component and combine computer vision with RAG.
# Maintenance scheduler: Generate service checklists and maintenance reminders based on mileage and manufacturer recommendations.
# Parts recommendations: Use parts catalogs to suggest compatible OEM part numbers for a specific vehicle.
# Step-by-step repair mode: Turn workshop procedures into interactive checklists so a mechanic can mark each step as completed.

# This progression takes the project from a document chatbot to a genuinely useful AI assistant for workshops and enthusiasts, while giving you hands-on experience with advanced RAG concepts like metadata filtering, hybrid search, multimodal retrieval, and tool integration.