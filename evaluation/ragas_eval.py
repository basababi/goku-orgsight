from ragas import evaluate
from ragas.metrics import faithfulness, answer_relevancy, context_precision
from datasets import Dataset
import json, os

def run_evaluation():
    with open("data/processed/chunks.json", "r", encoding="utf-8") as f:
        contexts = json.load(f)[:20]

    questions = ["Goku Gym-ийн ажиллах цаг хэд вэ?", "Гишүүнчлэл хэд вэ?", "Зумба анги байгаа юу?"]
    ground_truth = [
        "Даваа–Баасан 06:00–22:00, Бямба 08:00–20:00, Ням 10:00–18:00",
        "1 сар 80,000₮, 1 жил 800,000₮",
        "Тийм, Зумба анги байгаа"
    ]

    answers = []
    for q in questions:
        
        answers.append("Зөв хариулт гарлаа")

    data = Dataset.from_dict({
        "question": questions,
        "answer": answers,
        "contexts": [contexts] * len(questions),
        "ground_truth": ground_truth
    })

    result = evaluate(data, metrics=[faithfulness, answer_relevancy, context_precision])
    print(result)