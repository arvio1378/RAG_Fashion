import os
import re
import pandas as pd
from langchain.schema import Document

# cleaning dataset
def clean_text(text):
    if pd.isna(text):
        return ""
    text = str(text)
    text = re.sub(r"[\n\t\r\xa0]", " ", text)
    text = re.sub(r"[^a-zA-Z0-9\s.,!?;:'\"()\-&/%+]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# load dataset and create documents
def load_documents(csv_path, image_folder):
    df = pd.read_csv(csv_path)

    df["description"] = df["description"].fillna(df["display_name"])
    df.loc[df["description"] == "-", "description"] = df["display_name"]

    df["text"] = (
        "Product Name: " + df["display_name"] + ". "
        "Description: " + df["description"] + ". "
        "Category: " + df["category"]
    )

    df["text"] = df["text"].apply(clean_text)
    df = df.dropna(subset=["text"])

    documents = []
    for row in df.itertuples(index=False):
        image_path = os.path.join(image_folder, row.image)
        if not os.path.exists(image_path):
            continue

        documents.append(
            Document(
                page_content=row.text,
                metadata={
                    "image_path": image_path,
                    "display_name": row.display_name,
                    "category": row.category
                }
            )
        )

    return documents
