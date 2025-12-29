from data_loader import load_documents
from indexer import build_faiss_index

docs = load_documents(
    csv_path="dataset/data.csv",
    image_folder="dataset/data"
)

build_faiss_index(docs)
print("✅ Index built successfully")