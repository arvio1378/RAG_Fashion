# RAG_Fashion

## 📋 Deskripsi
Fashion RAG (Retrieval-Augmented Generation) adalah proyek AI/ML yang menggabungkan retrieval berbasis data produk fashion dengan Large Language Model (LLM) untuk memberikan rekomendasi fashion yang akurat, relevan, dan konsisten berdasarkan data yang tersedia. Proyek ini dirancang untuk menjawab pertanyaan pengguna (teks) dan menampilkan produk fashion beserta gambar secara terkontrol, tanpa menambahkan informasi di luar data.

## 🚀 Fitur
- Dataset disimpan dalam bentuk CSV
- Menjawab pertanyaan seputar produk Fashion
- Antarmuka sederhana menggunakan Gradio
- Multimodal output (teks + gambar)
- Fast inference (optimized loading & caching)

## 🧠 Tools & Library
- Python
- Langchain
- Pandas
- Numpy
- Transformers
- Json
- Ollama
- PIL
- tqdm
- faiss
- Gradio
- Torch
- LLM Model : qwen2.5:0.5b
- Embedding Model : laion/CLIP-ViT-B-32-laion2B-s34B-b79K

## 📦 Konsep Utama
Fashion RAG bekerja dengan alur berikut:
1. User Query
- Pengguna memasukkan pertanyaan, misalnya: "Can you show me a yellow gloves?"
2. Retriever
- Sistem mencari produk paling relevan dari dataset fashion (metadata + embedding).
3. Context Injection
- Informasi produk yang ditemukan diberikan ke LLM sebagai context.
4. LLM Generation
- LLM menghasilkan jawaban hanya berdasarkan data produk yang diberikan.
5. Multimodal Output : Teks & Galeri gambar produk

## 📁 Struktur Folder
- FASHION RAG/
  - data
      - data.csv
      - data
          - 1.jpg
          - 2.jpg
          - 3.jpg
  - index
      - faiss_index.bin
      - metadata.json
  - src
      - __init__.py
      - data_loader.py
      - embedder.py
      - indexer.py
      - llm.py
      - rag.py
      - retriever.py
      - main.py
  - build_index.py
  - test.ipynb
  - requirements.txt
  - README.md
