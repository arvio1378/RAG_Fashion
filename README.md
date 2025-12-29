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
1. User Query : Pengguna memasukkan pertanyaan, misalnya: "Can you show me a yellow gloves?"
2. Retriever : Sistem mencari produk paling relevan dari dataset fashion (metadata + embedding).
3. Context Injection : Informasi produk yang ditemukan diberikan ke LLM sebagai context.
4. LLM Generation : LLM menghasilkan jawaban hanya berdasarkan data produk yang diberikan.
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

## 🛠️ Workflow
1. Load dataset
2. Cleaning data
3. Membuat dokumen dari csv
4. Embedding : mengubah teks menjadi vektor angka
5. Vector store : menyimpan hasil embedding ke vector database
6. Retriever : mencari dari vector database hasil yang paling mirip untuk diambil
7. LLM : Memproses jawaban dari konteks kemiripan dari retriever
- Mengapa Tidak Menggunakan Chunking?
Sistem ini tidak menggunakan chunking teks karena setiap entri data mewakili satu produk dengan gambarnya sendiri. Chunking biasanya diperlukan untuk dokumentasi yang panjang, sedangkan deskripsi produk sudah atomik dan lengkap secara semantik. Selain itu, CLIP membutuhkan keselarasan yang kuat antara teks dan gambar dan juga memisahkan teks menjadi beberapa bagian akan melemahkan hubungan multimodal ini dan mengurangi kualitas pengambilan data.

## 🖥️ Cara Menjalankan Program
1. Clone repositori
```bash
git clone https://github.com/arvio1378/Apple-QA-RAG.git
cd Apple QA RA
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Jalankan Program
```bash
python src/main.py
```
