from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_answer(query: str, contexts: list):
    if not contexts:
        return "Мэдээлэл олдсонгүй."

  
    context_str = "\n\n---\n\n".join(contexts)

    prompt = f"""Та Goku Gym-ийн албан ёсны туслах юм.
Зөвхөн доорх мэдээлэл дээр тулгуурлан Монгол хэлээр, богино бөгөөд тодорхой хариулна уу.
Хэрэв мэдээлэл байхгүй бол "Мэдээлэл байхгүй" гэж хариулна уу.
Эх сурвалж зааж, [1], [2] гэж бичэхгүй.

Мэдээлэл:
{context_str}

Асуулт: {query}

Хариулт:"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2,
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"Алдаа гарлаа: {e}"
