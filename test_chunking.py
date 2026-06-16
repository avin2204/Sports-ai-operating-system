from app.rag.chunkers.recursive_chunker import (
    RecursiveChunker
)

text = """
Virat Kohli scored 973 runs in IPL.
RCB reached playoffs.
Rohit Sharma scored 600 runs.
Messi scored 25 goals.
Liverpool won 3-0.
""" * 200

chunker = RecursiveChunker()

chunks = chunker.chunk(text)

print("=" * 50)
print(f"Chunks Created: {len(chunks)}")
print("=" * 50)

for index, chunk in enumerate(chunks[:3]):

    print(f"\nChunk {index + 1}")
    print("-" * 30)

    print(chunk[:300])