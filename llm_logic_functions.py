import google.generativeai as genai
import subprocess
import json
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def gemini_embedding(text: str):
    response = genai.embed_content(
        model="gemini-embedding-001",
        content=text,
        task_type="retrieval_query"
    )
    return response['embedding']


def ollama_query_model(prompt: str) -> str:
    """Запрос к модели ollama"""
    model_name = 'llama3.1:8b'
    cmd = ["ollama", "run", model_name]
    process = subprocess.Popen(
        cmd,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )
    stdout, stderr = process.communicate(prompt, timeout=60)

    responses = []
    for line in stdout.splitlines():
        try:
            data = json.loads(line)
            if "response" in data:
                responses.append(data["response"])
        except json.JSONDecodeError:
            responses.append(line.strip())

    text = " ".join(responses).strip()
    if not text:
        text = stdout.strip()

    return text


def gemini_query_model(prompt: str, model_name='models/gemini-2.5-flash-lite') -> str:
    """
    Запрос к модели Google AI Studio (Gemini) вместо Ollama.
    """
    try:
        model = genai.GenerativeModel(model_name)
        response = model.generate_content(prompt)

        if hasattr(response, "text"):
            return response.text.strip()
        elif hasattr(response, "candidates") and len(response.candidates) > 0:
            return response.candidates[0].content.parts[0].text.strip()
        else:
            return str(response).strip()

    except Exception as e:
        print(f"Ошибка при обращении к Google AI Studio: {e}")
        return ""