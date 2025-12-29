import ollama

# LLM model
def generate_answer(prompt):
    res = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )
    return res["message"]["content"]
