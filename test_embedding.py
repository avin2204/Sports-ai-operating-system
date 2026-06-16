from app.rag.embeddings.local_embedding import (
    LocalEmbedding
)

embedding = LocalEmbedding()

vector = embedding.embed(
    "Virat Kohli scored 973 runs"
)

print(len(vector))