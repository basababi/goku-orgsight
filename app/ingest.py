import fitz, os
from docx import Document

def read_file(path):
    ext = os.path.splitext(path)[1].lower()
    if ext == ".pdf":
        doc = fitz.open(path)
        return "\n".join([p.get_text() for p in doc])
    elif ext in [".docx", ".doc"]:
        doc = Document(path)
        return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
    else:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
