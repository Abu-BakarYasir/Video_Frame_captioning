# 📁 captioner.py
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
import base64
import requests
import io

def image_to_base64(pil_image):
    buffered = io.BytesIO()
    pil_image.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode("utf-8")

# def get_caption_from_groq(pil_image, api_key):
#     url = "https://api.groq.com/v1/vision/caption"  # Placeholder, replace with actual Groq endpoint
#     headers = {
#         "Authorization": f"Bearer {api_key}",
#         "Content-Type": "application/json"
#     }
#     data = {
#         "image": image_to_base64(pil_image),
#         "task": "caption"
#     }
#     response = requests.post(url, json=data, headers=headers)
#     return response.json().get("caption", "No caption generated.")

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
def get_caption_from_groq(pil_image, api_key=None):
    inputs = processor(pil_image, return_tensors="pt")
    out = model.generate(**inputs)
    return processor.decode(out[0], skip_special_tokens=True)