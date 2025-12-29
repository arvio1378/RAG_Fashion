from retriever import search_by_text
from llm import generate_answer

# Create prompt for LLM
def build_prompt(query, docs):
    context = "\n".join(
        f"""
Product {i+1}:
Name: {d['display_name']}
Category: {d['category']}
"""
        for i, d in enumerate(docs)
    )

    return f"""
You are a professional fashion assistant.

Rules:
- Use ONLY the products listed below
- Do NOT invent products
- You MUST mention ALL listed products in your answer

Available products ({len(docs)} items):
{context}

User request:
{query}

Task:
- Briefly explain each product
- Mention style and usage occasion
- Assume images are shown in the same order

Answer:
"""

# Process result
def ask_rag(question, k=3):
    docs = search_by_text(question, k)
    answer = generate_answer(build_prompt(question, docs))
    return answer, docs