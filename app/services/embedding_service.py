class EmbeddingService:

    def __init__(self):

        from app.rag.embeddings.local_embedding import (
            LocalEmbedding
        )

        self.embedding_model = (
            LocalEmbedding()
        )

    def embed(
        self,
        text: str
    ):

        return self.embedding_model.embed(
            text
        )