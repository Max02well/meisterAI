# from langchain_community.document_loaders import PyPDFLoader
# loader = PyPDFLoader("data/manuals/engine/VWUSA.COM_SSP_401_1.8L_TFSI_Engine_16V.pdf")

# documents = loader.load()

from pathlib import Path
from src.utils.metadata_parser import extract_metadata
from langchain_community.document_loaders import PyMuPDFLoader

print(Path.cwd())


def load_documents(data_path="data/manuals"):
    documents = []

    pdf_files = list(Path(data_path).rglob("*.pdf"))
    print(f"Found {len(pdf_files)} PDF files in {data_path}")
    print(pdf_files)

    for pdf in pdf_files:
        print(f"\nLoading {pdf}")

        loader = PyMuPDFLoader(str(pdf))
        docs = loader.load()
        print(f"Loaded {len(docs)} pages from {pdf}")
       
        metadata = extract_metadata(pdf)
        for doc in docs:
            # doc.metadata["source"] = str(pdf)
            doc.metadata = {
                **metadata,
                "page": doc.metadata.get("page", 0)
            }

        documents.extend(docs)

    print(f"\nLoaded {len(documents)} pages total")

    return documents