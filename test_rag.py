from app.rag.embeddings.local_embedding import (
    LocalEmbedding
)

from app.rag.vectorstores.qdrant_vector_store import (
    QdrantVectorStore
)

from app.providers.gemini_provider import (
    GeminiProvider
)


embedding_model = LocalEmbedding()

vector_store = QdrantVectorStore()

llm = GeminiProvider()


question = "Who scored most runs in IPL 2016?"


query_vector = embedding_model.embed(
    question
)


results = vector_store.search(
    embedding=query_vector,
    top_k=3
)


context = "\n".join(
    hit.payload["text"]
    for hit in results
)


prompt = f"""
Answer the question using the context below.

Context:
{context}

Question:
{question}

Answer:
"""


answer = llm.generate(
    prompt
)


print("\nQUESTION:")
print(question)

print("\nCONTEXT:")
print(context)

print("\nANSWER:")
print(answer)