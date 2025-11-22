from fastapi import FastAPI
import json, os

app = FastAPI()

@app.get("/search")
def search(q: str = ""):
    if not os.path.exists("data/processed/chunks.json"):
        return {"error": "Индекс байхгүй. python scripts/run_index.py ажиллуулна уу"}
    with open("data/processed/chunks.json", "r", encoding="utf-8") as f:
        chunks = json.load(f)
    results = [c for c in chunks if q.lower() in c.lower()][:5]
    return {"results": results}
