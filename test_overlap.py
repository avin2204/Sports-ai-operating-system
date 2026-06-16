from app.rag.chunkers.recursive_chunker import (
    RecursiveChunker
)

text = "Virat Kohli scored runs. " * 500

chunker = RecursiveChunker()

chunks = chunker.chunk(text)

print("Chunk Count:", len(chunks))

print("\nLast 100 chars of Chunk 1:")
print(chunks[0][-100:])

print("\nFirst 100 chars of Chunk 2:")
print(chunks[1][:100])