# 🎥 Video Captioning & Summarization App

This is a **Streamlit-powered AI application** that:
- Extracts frames from an uploaded video every 2 seconds
- Uses **Groq Vision AI** (via Groq API) to **generate image captions** for each frame
- Summarizes all captions into a concise description using an LLM
- Displays the frames alongside their captions and the final summary

---

## 🚀 Features

- 🔍 Automatic **frame extraction** (every 2 seconds)
- 🧠 **Groq Vision AI**-based image captioning
- ✍️ **Groq LLM**-powered summarization of all captions
- 🖼️ Interactive UI with **Streamlit**
- 📦 Modular Python files for better readability

---

## 🧱 Project Structure

```

Video Captioning App/
│
├── app.py                # Streamlit UI
├── extractor.py          # Extracts frames from video
├── generator.py          # Sends frames to Groq Vision model for captions
├── summarizer.py         # Summarizes all captions into text
├── requirements.txt      # Project dependencies
├── .env                  # Your API keys (excluded via .gitignore)
└── .gitignore            # Ignore files/folders for Git

````

---

## 🧪 Demo Preview



https://github.com/user-attachments/assets/893352f5-0a85-41c8-8848-4caf5d10bf3e



---

## ⚙️ Requirements

- Python 3.9+
- A Groq API key with Vision model access

Install dependencies:

```bash
pip install -r requirements.txt
````

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_api_key_here
```

---

## 🧠 How It Works

1. **Video Upload**: User uploads a video file via Streamlit.
2. **Frame Extraction**: `frame_extractor.py` extracts frames every 2 seconds.
3. **Captioning**: `caption_generator.py` sends each frame to the Groq Vision endpoint and retrieves a caption.
4. **Summarization**: `summarizer.py` takes all captions and generates a single meaningful summary using the Groq LLM.
5. **Display**: All frames with their captions and the final summary are rendered in the Streamlit app.

---

## 📦 API Endpoints Used

* **Groq Chat LLM (Text Summarization)**
  `https://api.groq.com/v1/chat/completions`

---

## 📁 Sample Output

```
📷 Frame 1: "A person standing near a river"
📷 Frame 2: "The same person walking on a bridge"
...

📝 Summary: "A person explores a riverside location, crossing a bridge and walking through natural scenery."
```



## 🙋‍♂️ Author

**Abu Bakar**
Computer Engineer @ COMSATS Lahore
Full Stack Developer | AI Enthusiast
[GitHub](https://github.com/Abu-BakarYasir)

---

## 📬 Feedback

Feel free to raise issues, open pull requests, or suggest features!

