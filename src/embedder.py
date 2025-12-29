import torch
import numpy as np
from PIL import Image as PILImage
from transformers import CLIPModel, CLIPProcessor

# Embedding Model
CLIP_NAME = "laion/CLIP-ViT-B-32-laion2B-s34B-b79K"
device = "cuda" if torch.cuda.is_available() else "cpu"

clip_model = CLIPModel.from_pretrained(CLIP_NAME).to(device)
clip_processor = CLIPProcessor.from_pretrained(CLIP_NAME)
clip_model.eval()

# embedding text
@torch.no_grad()
def embed_texts(texts):
    inputs = clip_processor(
        text=texts,
        padding=True,
        truncation=True,
        return_tensors="pt"
    ).to(device)

    emb = clip_model.get_text_features(**inputs)
    emb = emb / emb.norm(dim=1, keepdim=True)
    return emb.cpu().numpy()

# embedding image
@torch.no_grad()
def embed_images(image_paths):
    images = [PILImage.open(p).convert("RGB") for p in image_paths]

    inputs = clip_processor(
        images=images,
        return_tensors="pt"
    ).to(device)

    emb = clip_model.get_image_features(**inputs)
    emb = emb / emb.norm(dim=1, keepdim=True)
    return emb.cpu().numpy()
