
import re
from typing import List


MN_STOPWORDS = {
    "ба", "бол", "байх", "байна", "буюу", "гэх", "гэдэг", "гэж", "энэ", "тэр", "би", "чи", "та",
    "тэд", "манай", "таны", "мөн", "гэвч", "харин", "тэгээд", "бас", "нь", "ын", "ийн", "д", "с",
    "өөр", "өөрөө", "ямар", "маш", "байдаг", "шаардлагатай", "эсвэл", "зэрэг", "дээр", "доор"
}


MN_SUFFIXES = sorted({
    "аас", "ээс", "оос", "өөс", "аар", "ээр", "оор", "өөр", "тай", "тэй", "той", "той", "руу", "рүү",
    "даа", "дээ", "доо", "дөө", "ын", "ийн", "ны", "ний", "ууд", "үүд", "ыг", "ийг"
}, key=len, reverse=True)

def mn_stem(word: str) -> str:
    """Энгийн Монгол stemming"""
    word = word.lower()
    for suffix in MN_SUFFIXES:
        if word.endswith(suffix):
            return word[:-len(suffix)]
    return word

def clean_text(text: str) -> str:
    """Текстийг цэвэрлэх + Монголд тохируулах"""
    text = re.sub(r"[^\w\s]", " ", text.lower())  
    text = re.sub(r"\s+", " ", text).strip()
    return text

def chunk_text(text: str, chunk_size: int = 250, overlap: int = 50) -> List[str]:
    words = text.split()
    chunks = []
    i = 0
    while i < len(words):
        chunk = " ".join(words[i:i + chunk_size])
        chunks.append(chunk)
        i += chunk_size - overlap
    return chunks

def preprocess_mongolian(text: str) -> List[str]:
    """Бүрэн Монгол preprocessing + stemming + stopword арилгах"""
    text = clean_text(text)
    words = text.split()
    processed = []
    for word in words:
        if word not in MN_STOPWORDS and len(word) >= 2:
            stemmed = mn_stem(word)
            if len(stemmed) >= 2:
                processed.append(stemmed)
    return processed