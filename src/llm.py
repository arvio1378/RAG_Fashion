import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

# LLM model
MODEL_NAME = "Qwen/Qwen2.5-0.5B"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    device_map="auto",
    dtype=torch.float16 if torch.cuda.is_available() else torch.float32
)

model.eval()


def generate_answer(prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    prompt_len = inputs["input_ids"].shape[1]

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=256,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.eos_token_id
        )

    generated_tokens = outputs[0][prompt_len:]
    return tokenizer.decode(generated_tokens, skip_special_tokens=True).strip()