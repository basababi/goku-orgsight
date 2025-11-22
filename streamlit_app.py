import streamlit as st
import requests, json, os
from reranker.cross_encoder import rerank
from app.generator import generate_answer

st.set_page_config(page_title="Goku ", layout="wide")
st.title("Goku ")
st.caption("PDF оруулаад асуулт асуугаарай ")

uploaded = st.file_uploader("PDF/DOCX/TXT оруулах", accept_multiple_files=True)
if uploaded:
    os.makedirs("data/raw", exist_ok=True)
    for f in uploaded:
        with open(f"data/raw/{f.name}", "wb") as out:
            out.write(f.getbuffer())
    if st.button("Индекс хийх"):
        with st.spinner("Индекс хийж байна..."):
            os.system("python scripts/run_index.py")
        st.success("Индекс бэлэн!")

query = st.text_input("Асуулт асууна уу:", placeholder="Goku Gym-ийн ням гаригт хэд хүртэл ажилладаг вэ?")
if st.button("Хайх)", type="primary") and query:
    with st.spinner("Хайж байна..."):
        try:
            
            with open("data/processed/chunks.json", "r", encoding="utf-8") as f:
                chunks = json.load(f)
           
            candidates = [c for c in chunks if any(word in c.lower() for word in query.lower().split())][:20]
            if candidates:
                ranked = rerank(query, candidates)
                answer = generate_answer(query, ranked)
                st.success("Хариу ирлээ!")
                st.write(answer)
            else:
                st.info("Мэдээлэл олдсонгүй")
        except Exception as e:
            st.error(f"Алдаа: {e}")
