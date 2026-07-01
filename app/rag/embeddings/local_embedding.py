class LocalEmbedding:

    def __init__(self):

        from sentence_transformers import (
            SentenceTransformer
        )

        self.model = SentenceTransformer(
            "all-MiniLM-L6-v2"
        )

    def embed(
        self,
        text: str
    ):

        return self.model.encode(
            text
        ).tolist()