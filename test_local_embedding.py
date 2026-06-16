from app.rag.embeddings.local_embedding import (
    LocalEmbedding
)

embedding = LocalEmbedding()

vector = embedding.embed(
    "Virat Kohli scored 973 runs in IPL"
)

print("=" * 50)
print("Embedding Generated")
print("=" * 50)

print(
    f"Vector Length: {len(vector)}"
)

print(
    vector[:5]
)