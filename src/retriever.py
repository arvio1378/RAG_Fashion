import faiss
import json
from embedder import embed_texts, embed_images

# load index
index = faiss.read_index("index/faiss_index.bin")
with open("index/metadata.json") as f:
    metadatas = json.load(f)

# text search
def search_by_text(query, k=5):
    q_emb = embed_texts([query]).astype("float32")
    scores, idx = index.search(q_emb, k)
    return [metadatas[i] for i in idx[0]]

# image search
def search_by_image(image_path, k=5):
    q_emb = embed_images([image_path]).astype("float32")
    scores, idx = index.search(q_emb, k)
    return [metadatas[i] for i in idx[0]]
