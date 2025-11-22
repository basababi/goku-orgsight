import os
from app.ingest import read_file
from app.preprocess import clean_text, chunk_text
from app.indexer import build_tfidf, build_embeddings, save_chunks

print("Баримтуудыг уншиж байна...")

texts = []
for filename in os.listdir("data/raw"):
    path = os.path.join("data/raw", filename)
    print(f"   {filename}")
    text = read_file(path)
    texts.append(text)

all_chunks = []
for text in texts:
    clean = clean_text(text)
    chunks = chunk_text(clean)
    all_chunks.extend(chunks)

print(f"Нийт {len(all_chunks)} chunk үүслээ")


build_tfidf(all_chunks)
build_embeddings(all_chunks)
save_chunks(all_chunks)

print("БҮГД БЭЛЭН БОЛЛОО! ")