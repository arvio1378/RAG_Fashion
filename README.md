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
git clone https://github.com/arvio1378/RAG_Fashion.git
cd RAG_Fashion
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Jalankan Program
```bash
python src/main.py
```
4. Buka Gradio di browser

## 📊 Dataset
| image    | description      | display_name | category |
|-------------|-------------|-------------|-------------|
| 3238.jpg	| Round toed, black sports shoes with red accent...	| Puma Men Black 65CC Lo Ducati Sports Shoes	| Sports Shoes |
| 43044.jpg	 | Style Note Built with the breathability and ze...	| Nike Men Charcoal Grey Shorts	| Shorts |
| 54018.jpg	 | Teal  handbag that has stitch detailing with a...	| Kiara Women Teal Handbag	| Handbags |

## 🧪 Aturan LLM
Berikut ini adalah aturan LLM yang digunakan :
- Hanya merekomendasikan 3 produk yang berkaitan
- Tidak mengarang tentang produknya
- Hanya merekomendasikan produk yang sesuai query
- Hanya menggunakan data yang diberikan
- Menjelaskan secara singkat dari produk yang berkaitan

## 📈 Hasil
Berikut ini adalah beberapa pertanyaan dan bagaimana model dapat menjawab pertanyaan tersebut.
1. - Question : I want to buy something casual watches for a weekend outing for men.
   - Answer : Carrera Men Careera (1.26mm), a stylish and durable watch with a rugged texture, is perfect for casual outings.
Q&Q Men Steel Dial Watch (1.48mm), known for its smooth finish and sleek design, is ideal for men's daily wear.
2. - Question : Can you show me red shirts ?
   - Answer : Product 1: Proline Men Red T-shirt - A classic and versatile t-shirt that is popular among men. It can be worn as a jacket, vest, or undergarment, making it suitable for both casual and formal occasions.
Style: Classic red shirt.
Usage: Ideal for working in offices or during business meetings where dress code is important. 
Product 2: Proline Men Red Round Neck T-shirt - This t-shirt features a round neck design that adds some privacy to the shirt without sacrificing comfort. It's great for lounging, playing sports, or reading a book.
Style: Round-necked red shirt.
Usage: Perfect for working out at gymnasiums where wearing too much clothing can be distracting. 
Product 3: Classic Polo Men's Red T-shirt - This t-shirt is a classic design that features large pockets and buttons around the neck, making it suitable for casual wear or any occasion.
Style: Classic red polo shirt.
Usage: Ideal for outdoor activities like hiking or camping where comfort matters.
Titan Men White Dial Watch (2.05mm) offers an elegant and sophisticated appearance that complements any outfit.
All three watches are made of high-quality steel materials, making them durable and long-lasting.
Q&Q Men Steel Dial Watch is a great option for those who want to add a touch of sophistication to their casual watches while maintaining durability.
Titan Men White Dial Watch features a sleek design with its black leather strap, making it suitable for men's daily wear.
3. - Question : I want to buy some shoes for men
   - Answer : Product 1 - ID Men Black Casual Shoes:
Style: Casual 
Usage: Suitable for daily wear or casual outings. Perfect for office wear, shopping trips, or any occasions where comfort is important.
Product 2 - iD Men Casual Brown Shoe:
Style: Casual
Usage: Ideal for daytime activities like running, working out, or everyday life. Great for hiking or outdoor workouts in the afternoon.
Product 3 - ADIDAS Men Black Shoes:
Style: Casual 
Usage: Perfect for casual wear occasions such as parties, weddings, or any social events. Suitable for various sports activities and casual outings where comfort is important.

## 🏗️ Kontribusi
Dapat melakukan kontribusi kepada siapa saja. Bisa bantu untuk :
- Menggunakan dataset yang lebih banyak dan kompleks
- Mencoba dengan model LLM yang berbeda
- Menyempurnakan desain dari gradio menjadi lebih bagus

## 🧑‍💻 Tentang Saya
Saya sedang belajar dan membangun karir di bidang AI/ML. Projek ini adalah latihan saya untuk membangun aplikasi python sederhana. Saya ingin lebih untuk mengembangkan skill saya di bidang ini melalui projek-projek yang ada.
📫 Terhubung dengan saya di:
- Linkedin : https://www.linkedin.com/in/arvio-abe-suhendar/
- Github : https://github.com/arvio1378
