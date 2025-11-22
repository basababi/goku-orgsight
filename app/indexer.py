
import joblib
import numpy as np
import faiss
import json
from sentence_transformers import SentenceTransformer
from app.preprocess import clean_text, chunk_text, preprocess_mongolian


model = SentenceTransformer("intfloat/multilingual-e5-base")

def build_tfidf(chunks):
    from sklearn.feature_extraction.text import TfidfVectorizer
    
    
    processed_chunks = [" ".join(preprocess_mongolian(chunk)) for chunk in chunks]
    
    vectorizer = TfidfVectorizer(
        lowercase=False,
        min_df=1,
        max_df=1.0,
        ngram_range=(1, 2)
    )
    
    X = vectorizer.fit_transform(processed_chunks)
    
    joblib.dump(vectorizer, "data/processed/tfidf_vectorizer.pkl")
    joblib.dump(X, "data/processed/tfidf_matrix.pkl")
    print(f"TF-IDF индекс бэлэн: {X.shape}")
    return vectorizer, X

def build_embeddings(chunks):
    print("Embedding үүсгэж байна... (1-2 минут хүлээнэ үү)")
    embeddings = model.encode(chunks, batch_size=16, show_progress_bar=True, normalize_embeddings=True).astype('float32')
    
    index = faiss.IndexFlatIP(embeddings.shape[1])
    index.add(embeddings)
    
    faiss.write_index(index, "data/processed/faiss.index")
    np.save("data/processed/embeddings.npy", embeddings)
    print(f"FAISS индекс бэлэн: {len(chunks)} chunk")
    return index

def save_chunks(chunks):
    with open("data/processed/chunks.json", "w", encoding="utf-8") as f:
        json.dump(chunks, f, ensure_ascii=False, indent=2)
    print(f"Chunks хадгаллаа: {len(chunks)} ширхэг")
