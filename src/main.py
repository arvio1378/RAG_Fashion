import gradio as gr
from rag import ask_rag
from PIL import Image

# Display result
def rag_ui(question):
    answer, docs = ask_rag(question)

    gallery_items = []
    for d in docs:
        img = Image.open(d["image_path"])
        caption = f"{d['display_name']} ({d['category']})"
        gallery_items.append((img, caption))

    return answer, gallery_items

# User Interface
with gr.Blocks() as demo:
    gr.Markdown("## 👕 Fashion Multimodal RAG")

    query = gr.Textbox(label="Ask for fashion product")
    answer = gr.Markdown()

    gallery = gr.Gallery(
        label="Retrieved Products",
        columns=3,
        height="auto"
    )

    btn = gr.Button("Search")

    btn.click(
        rag_ui,
        inputs=query,
        outputs=[answer, gallery]
    )

demo.launch()