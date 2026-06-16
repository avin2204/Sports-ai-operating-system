from app.rag.embeddings.local_embedding import (
    LocalEmbedding
)

from app.rag.vectorstores.qdrant_vector_store import (
    QdrantVectorStore
)

embedding_model = LocalEmbedding()

vector_store = QdrantVectorStore()

text = "Virat Kohli scored 973 runs in IPL 2016"

vector = embedding_model.embed(text)

vector_store.add(
    text=text,
    embedding=vector
)

print("Vector Stored Successfully")