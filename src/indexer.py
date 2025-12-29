import faiss
import json
import numpy as np
from tqdm import tqdm
from embedder import embed_texts, embed_images

# Build index
def build_faiss_index(documents, batch_size=32, save_dir="index"):
    vectors = []
    metadatas = []

    for i in tqdm(range(0, len(documents), batch_size)):
        batch = documents[i:i+batch_size]
        texts = [d.page_content for d in batch]
        images = [d.metadata["image_path"] for d in batch]

        text_emb = embed_texts(texts)
        image_emb = embed_images(images)

        emb = (text_emb + image_emb) / 2.0
        vectors.append(emb.astype("float32"))
        metadatas.extend([d.metadata for d in batch])

    vectors = np.vstack(vectors)
    dim = vectors.shape[1]

    index = faiss.IndexFlatIP(dim)
    index.add(vectors)

    faiss.write_index(index, f"{save_dir}/faiss_index.bin")
    with open(f"{save_dir}/metadata.json", "w") as f:
        json.dump(metadatas, f)

    print("✅ FAISS index saved")
