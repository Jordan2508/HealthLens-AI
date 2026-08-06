# 🩺 HealthLens AI

> **An AI-powered medical assistant that analyzes medical images, understands patient symptoms through voice, and generates intelligent diagnosis with voice responses.**

## 🚀 Features

- 📷 Medical Image Analysis using Groq Vision
- 🎤 Speech-to-Text with Groq Whisper
- 🧠 AI-powered Medical Diagnosis
- 🔊 Text-to-Speech using Google gTTS
- 💻 Interactive Streamlit Web App
- ⚡ Fast and lightweight AI pipeline

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Groq API
- Qwen 3.6-27B
- Groq Whisper
- Google gTTS
- SpeechRecognition
- PyDub

---

## 📂 Project Structure

```
HealthLens-AI/
│── app.py
│── brain_of_the_doctor.py
│── voice_of_the_patient.py
│── voice_of_the_doctor.py
│── requirements.txt
│── packages.txt
│── .env
└── README.md
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/HealthLens-AI.git
cd HealthLens-AI
```

Create a virtual environment

```bash
python -m venv .venv
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
streamlit run app.py
```

---

## 🔄 Workflow

```
Patient Voice
      │
      ▼
Speech-to-Text (Groq Whisper)
      │
      ▼
Medical Image + Symptoms
      │
      ▼
Groq Vision + LLM
      │
      ▼
Medical Diagnosis
      │
      ▼
Google gTTS
      │
      ▼
Voice Response
```

---

## 🎯 Future Enhancements

- 🩻 X-Ray & MRI Analysis
- ❤️ ECG Report Analysis
- 📄 PDF Medical Reports
- 🌍 Multi-language Support
- 📱 Mobile Application

---

## ⚠️ Disclaimer

This project is developed for **educational and research purposes only**. It is **not a substitute for professional medical advice, diagnosis, or treatment.**

---

## 👨‍💻 Author

**Bhavya Sharma**

B.Tech Artificial Intelligence & Machine Learning

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
