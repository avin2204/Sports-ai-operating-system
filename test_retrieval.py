from app.rag.embeddings.local_embedding import (
    LocalEmbedding
)

from app.rag.vectorstores.qdrant_vector_store import (
    QdrantVectorStore
)

embedding_model = LocalEmbedding()

vector_store = QdrantVectorStore()

query = "Who scored most runs for RCB?"

query_vector = embedding_model.embed(query)

results = vector_store.search(
    embedding=query_vector,
    top_k=3
)

print("\nResults:\n")

for result in results:

    print(result.payload)