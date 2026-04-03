import requests
import time
from config import OPENROUTER_API_KEY

def call_llm(prompt, context):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json",
        "HTTP-Referer": "http://localhost",
        "X-Title": "Agentic RAG Project"
    }

    final_prompt = f"""
Answer using context.

Context:
{context}

Question:
{prompt}
"""

    models = [
        "mistralai/mistral-7b-instruct:free",
        "meta-llama/llama-3.2-3b-instruct:free",
        "openrouter/auto"
    ]

    for model in models:
        for _ in range(2):
            try:
                response = requests.post(url, headers=headers, json={
                    "model": model,
                    "messages": [{"role": "user", "content": final_prompt}]
                })

                result = response.json()

                if "choices" in result:
                    return result["choices"][0]["message"]["content"]

                if "error" in result and result["error"].get("code") == 429:
                    time.sleep(2)
                    continue

            except:
                continue

    # 🔥 FINAL GUARANTEED OUTPUT
    return f"""
[Fallback RAG Response]

{context}
"""
