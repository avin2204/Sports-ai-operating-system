class ChunkingService:

    def __init__(self):

        from langchain_text_splitters import (
            RecursiveCharacterTextSplitter
        )

        self.splitter = (
            RecursiveCharacterTextSplitter(
                chunk_size=1000,
                chunk_overlap=200
            )
        )

    def chunk(
        self,
        text: str
    ):

        return self.splitter.split_text(
            text
        )