# 📁 summarizer.py
import requests

def summarize_captions(captions, api_key):
    prompt = "\n".join(captions) + "\n\nSummarize what is happening in this video."
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-70b-8192",
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    response = requests.post(url, json=payload, headers=headers)

    try:
        return response.json()['choices'][0]['message']['content']
    except Exception as e:
        print("Groq API response error:", response.text)
        return "⚠️ Failed to summarize captions."
