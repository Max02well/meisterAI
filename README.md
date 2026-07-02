# MeisterAI

> **Your Intelligent German Vehicle Maintenance & Repair Assistant**

MeisterAI is an AI-powered Retrieval-Augmented Generation (RAG) application designed to assist mechanics, automotive technicians, enthusiasts, and workshop owners in diagnosing, maintaining, and repairing **German vehicles** such as **BMW, Audi, Mercedes-Benz, Volkswagen, Porsche**.

Instead of relying on traditional keyword searches, MeisterAI uses **semantic search** powered by vector embeddings to retrieve the most relevant information from workshop manuals, owner manuals, technical service bulletins, diagnostic guides, and maintenance documentation before generating an intelligent response using a Large Language Model (LLM).

---

# Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Project Architecture](#project-architecture)
- [Folder Structure](#folder-structure)
- [Technology Stack](#technology-stack)
- [Packages Used](#packages-used)
- [Knowledge Base](#knowledge-base)
- [How RAG Works](#how-rag-works)
- [Future Roadmap](#future-roadmap)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [License](#license)

---

# Overview

Finding reliable repair procedures for modern German vehicles can be difficult due to the complexity of their systems and the amount of technical documentation available.

MeisterAI solves this by acting as an intelligent workshop assistant capable of answering questions such as:

- How do I replace the timing chain on a BMW N47?
- What engine oil should an Audi A4 B9 use?
- Explain OBD-II code P0171.
- What causes VANOS failure?
- Show the torque specifications for BMW N55 spark plugs.
- Compare Ceramic vs Carbon tint recommendations.
- How do I perform DPF regeneration?

Instead of generating answers from memory, MeisterAI retrieves the most relevant documentation first and then generates grounded responses based on those sources.

---

# Features

## Intelligent Semantic Search

Search manuals using natural language instead of exact keywords.

Example:

```
My BMW won't start after replacing the battery.
```

instead of

```
BMW Battery Registration Procedure
```

---

## Retrieval-Augmented Generation (RAG)

Uses vector search to retrieve the most relevant repair procedures before generating responses.

---

## Vehicle-Specific Knowledge

Supports:

- BMW
- Audi
- Mercedes-Benz
- Volkswagen
- Porsche
- Škoda

---

## Workshop Manual Search

Search across

- Owner Manuals
- Workshop Manuals
- Service Manuals
- Maintenance Guides
- Technical Service Bulletins
- Parts Catalogues
- OBD-II Documentation

---

## AI-Powered Repair Assistance

Ask questions naturally such as

- Why is my engine overheating?
- Explain code P0420.
- How do I replace brake pads?
- Where is the fuel filter located?
- Recommended oil viscosity?

---

## Source Citation

Every response includes the source manual or document used to generate the answer.

---

## Metadata Filtering

Retrieve documents by:

- Vehicle Brand
- Model
- Engine
- Year
- Category
- Manual Type

---

##  Fast Vector Search

Uses ChromaDB for lightning-fast semantic retrieval.

---

# Project Architecture

```
                     User Question
                           │
                           ▼
                     Embedding Model
                           │
                           ▼
                    Chroma Vector Store
                           │
                  Retrieve Relevant Chunks
                           │
                           ▼
                  Large Language Model
                           │
                           ▼
                 AI Generated Response
```

---

# Folder Structure

```
meisterAI/
│
├── data/
│   ├── manuals/
│   │   ├── bmw/
│   │   ├── audi/
│   │   ├── mercedes/
│   │   ├── volkswagen/
│   │   ├── porsche/
│   │   └── skoda/
│   │
│   ├── obd/
│   │
│   ├── maintenance/
│   │
│   └── service_bulletins/
│
├── chroma_db/
│
├── models/
│
├── notebooks/
│
├── src/
│   │
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   ├── embedder.py
│   │   └── ingest.py
│   │
│   ├── retrieval/
│   │   ├── retriever.py
│   │   ├── reranker.py
│   │   └── prompts.py
│   │
│   ├── api/
│   │   └── api.py
│   │
│   ├── utils/
│   │
│   └── config.py
│
├── tests/
│
├── main.py
│
├── pyproject.toml
│
├── README.md
│
└── .gitignore
```

---

# Technology Stack

| Layer | Technology |
|---------|------------|
| Backend | FastAPI |
| Language | Python 3.13+ |
| Vector Database | ChromaDB |
| Embedding Model | Sentence Transformers / ONNX MiniLM |
| AI | OpenAI / Gemini / Ollama (Future) |
| Document Processing | LangChain |
| Data Handling | Pandas |
| Machine Learning | Scikit-Learn |
| API Server | Uvicorn |
| Package Manager | uv |

---

# Packages Used

## Core

```
fastapi
uvicorn
chromadb
langchain
langchain-community
langchain-text-splitters
sentence-transformers
```

---

## Document Processing

```
pypdf
pymupdf
python-docx
beautifulsoup4
markdown
```

---

## Machine Learning

```
numpy
pandas
scikit-learn
joblib
```

---

## Utilities

```
python-dotenv
tqdm
requests
```

---

## Development

```
jupyter
ipykernel
pytest
black
```

---

# Knowledge Base

The AI retrieves information from

```
BMW Owner Manuals

BMW Workshop Manuals

Audi Repair Manuals

Mercedes Technical Documentation

Volkswagen Workshop Guides

Porsche Service Manuals

OBD-II Codes

Torque Specifications

Oil Specifications

Maintenance Guides

Technical Service Bulletins

Parts Catalogues
```

---

# Example Metadata

Every chunk stored inside ChromaDB contains metadata such as:

```json
{
    "brand": "BMW",
    "model": "F30",
    "engine": "N47",
    "year": 2015,
    "category": "Engine",
    "section": "Timing Chain",
    "source": "BMW Workshop Manual"
}
```

This allows MeisterAI to retrieve only the most relevant documents.

---

# How RAG Works

## Step 1

Load workshop manuals.

↓

## Step 2

Split documents into chunks.

↓

## Step 3

Generate embeddings.

↓

## Step 4

Store embeddings inside ChromaDB.

↓

## Step 5

User asks a question.

↓

## Step 6

Retrieve the most relevant chunks.

↓

## Step 7

Send retrieved context to the LLM.

↓

## Step 8

Generate an accurate response with citations.

---

# Future Roadmap

## Phase 1

- PDF ingestion
- ChromaDB indexing
- Semantic search
- FastAPI backend

---

## Phase 2

- Multi-document retrieval
- Metadata filtering
- Conversation memory
- Source citations

---

## Phase 3

- React frontend
- Authentication
- User uploads
- Chat history

---

## Phase 4

- Image-based diagnostics
- Dashboard warning light recognition
- VIN decoder
- OBD-II scanner integration
- Repair procedure recommendations

---

## Phase 5

- Multimodal RAG
- Voice assistant
- Mobile application
- Offline mode
- Workshop management integration

---

# Installation

Clone the repository

```bash
git clone https://github.com/Max02well/meisterAI.git

cd meisterAI
```

Create a virtual environment

```bash
uv venv
```

Activate the environment

Windows

```powershell
.venv\Scripts\Activate.ps1
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
uv sync
```

---

# Running the Project

Start the FastAPI server

```bash
python main.py
```

or

```bash
uvicorn src.api:app --reload
```

API Documentation

```
http://localhost:8000/docs
```

---

# Future Integrations

- OpenAI GPT
- Google Gemini
- Ollama
- DeepSeek
- Claude
- Hugging Face
- Elasticsearch Hybrid Search

---

# License

MIT License

---

# Author

**Maxwell Gogo**

AI/ML Engineer | Full Stack Developer

Building intelligent AI solutions for the automotive industry using Retrieval-Augmented Generation (RAG), FastAPI, Vector Databases, and Large Language Models.

---

> **"Knowledge is only useful when it can be retrieved at the right time."**
>
> — MeisterAI