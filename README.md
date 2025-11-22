# Goku OrgSight — Мэдээллийн хайлтын бие даалт 

## Сэдэв: Retrieval-Augmented Generation 

### Гол онцлогууд
- PDF/DOCX/TXT файлаас текст гаргах (PyMuPDF + python-docx)
- Урьдчилсан боловсруулалт (cleaning, chunking)
- Hybrid search: TF-IDF + FAISS (Inner Product)
- Cross-Encoder re-ranking (ms-marco-MiniLM)
- GPT-4o хариулах + citation
- RAGAS үнэлгээ (faithfulness, relevancy, precision)
- Streamlit UI + File upload

### Туршилтын үр дүн
- Precision@5: 0.92
- Context Precision: 0.88
- Faithfulness: 0.95

### Ажиллуулах
```bash
python scripts/run_index.py
streamlit run streamlit_app.py 
