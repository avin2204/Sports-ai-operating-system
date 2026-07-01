from app.rag.loaders.text_loader import TextLoader
from app.rag.chunkers.fixed_chunker import FixedChunker
from app.rag.embeddings.local_embedding import (
    LocalEmbedding
)
from app.rag.vectorstores.qdrant_vector_store import (
    QdrantVectorStore
)
from app.rag.prompts.prompt_builder import (
    PromptBuilder
)

from app.providers.gemini_provider import (
    GeminiProvider
)


class RAGService:

    def __init__(self):

        self.loader = TextLoader()

        self.chunker = FixedChunker()

        self.prompt_builder = (
            PromptBuilder()
        )

        self.llm = GeminiProvider()

        self.embedding_model = LocalEmbedding()

        self.vector_store = (
            QdrantVectorStore()
        )

    def ingest(
        self,
        file_path: str
    ):

        text = self.loader.load(
            file_path
        )

        chunks = self.chunker.chunk(
            text
        )

        for chunk in chunks:

            embedding = (
                self.embedding_model.embed(
                    chunk
                )
            )

            self.vector_store.add(
                text=chunk,
                embedding=embedding
            )

    def retrieve(
        self,
        query: str
    ):

        query_embedding = (
            self.embedding_model.embed(
                query
            )
        )

        results = (
            self.vector_store.search(
                embedding=query_embedding
            )
        )

        return results
    
    def ask(
        self,
        question: str
    ) -> str:

        contexts = self.retrieve(
            question
        )

        prompt = (
            self.prompt_builder.build(
                question=question,
                contexts=contexts
            )
        )

        answer = (
            self.llm.generate(
                prompt
            )
        )

        return answer