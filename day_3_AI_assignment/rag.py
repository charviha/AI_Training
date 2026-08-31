import os

SYSTEM_CA = "/etc/ssl/certs/ca-certificates.crt"

os.environ["REQUESTS_CA_BUNDLE"] = SYSTEM_CA
os.environ["SSL_CERT_FILE"] = SYSTEM_CA
os.environ["CURL_CA_BUNDLE"] = SYSTEM_CA

print("Using certificate bundle:", SYSTEM_CA)

from sentence_transformers import SentenceTransformer
import faiss
import numpy as np


# -----------------------------
# 1. Load embedding model
# -----------------------------

model = SentenceTransformer("all-MiniLM-L6-v2")


# -----------------------------
# 2. Read documents
# -----------------------------

DATA_FOLDER = "data"

documents = []

for root, dirs, files in os.walk(DATA_FOLDER):
    for file in files:
        if file.endswith(".txt"):
            file_path = os.path.join(root, file)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            documents.append({
                "text": text,
                "source": file
            })


print("Documents loaded:", len(documents))


# -----------------------------
# 3. Create chunks
# -----------------------------

chunks = []

for document in documents:

    text = document["text"]
    source = document["source"]

    # Simple paragraph-based chunking
    paragraphs = text.split("\n\n")

    for paragraph in paragraphs:

        paragraph = paragraph.strip()

        if paragraph:
            chunks.append({
                "text": paragraph,
                "source": source
            })


print("Chunks created:", len(chunks))


# -----------------------------
# 4. Generate embeddings
# -----------------------------

texts = [chunk["text"] for chunk in chunks]

embeddings = model.encode(
    texts,
    convert_to_numpy=True
)

print("Embedding shape:", embeddings.shape)


# -----------------------------
# 5. Normalize embeddings
# -----------------------------

faiss.normalize_L2(embeddings)


# -----------------------------
# 6. Create FAISS index
# -----------------------------

dimension = embeddings.shape[1]

index = faiss.IndexFlatL2(dimension)

index.add(embeddings)

print("Vectors stored in FAISS:", index.ntotal)


# -----------------------------
# 7. Search function
# -----------------------------

def search_documents(query, k=3):

    query_embedding = model.encode(
        [query],
        convert_to_numpy=True
    )

    faiss.normalize_L2(query_embedding)

    distances, indices = index.search(
        query_embedding,
        k
    )

    results = []

    for distance, idx in zip(distances[0], indices[0]):

        results.append({
            "score": float(distance),
            "text": chunks[idx]["text"],
            "source": chunks[idx]["source"]
        })

    return results


# -----------------------------
# 8. Test search
# -----------------------------

if __name__ == "__main__":

    query = "What are Acme's main concerns?"

    results = search_documents(query)

    print("\nSearch Query:")
    print(query)

    print("\nTop Results:")

    for rank, result in enumerate(results, start=1):

        print("\nRank:", rank)
        print("Score:", round(result["score"], 4))
        print("Source:", result["source"])
        print("Matched Text:", result["text"])
