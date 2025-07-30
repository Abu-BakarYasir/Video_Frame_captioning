# 📁 app.py
import streamlit as st
from dotenv import load_dotenv
from frame_extractor import extract_frames
from captioner import get_caption_from_groq
from summarizer import summarize_captions
import tempfile
import os

load_dotenv()
st.title("🎥 Video Frame Captioning and Summary (Groq Vision AI)")
try:
    api_key = st.secrets["GROQ_API_KEY"]
except AttributeError:
    # st.secrets might not exist locally
    api_key = os.getenv("GROQ_API_KEY")
except KeyError:
    api_key = os.getenv("GROQ_API_KEY")


uploaded_file = st.file_uploader("Upload a .mp4 video", type=["mp4"])
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as tmp:
        tmp.write(uploaded_file.read())
        tmp_path = tmp.name

    st.info("Extracting frames every 2 seconds...")
    frames = extract_frames(tmp_path, interval_sec=2)

    captions = []
    for timestamp, frame in frames:
        st.image(frame, caption=f"⏱ Time: {timestamp}s")
        caption = get_caption_from_groq(frame, api_key)
        captions.append(caption)
        st.markdown(f"**Caption:** {caption}")

    if st.button("Generate Summary"):
        st.info("Generating summary with Groq LLM...")
        summary = summarize_captions(captions, api_key)
        st.success("Video Summary:")
        st.write(summary)