# Explainify 🧠✨

Explainify is an AI-powered concept explainer built with Streamlit and Hugging Face.  
Enter any concept, choose an explanation style and length, and get an instant clear explanation from an open-source language model.

---

## 🚀 Features

- Custom concept input  
- Multiple explanation styles  
- Adjustable explanation length  
- Hugging Face powered open-source LLM  
- Simple Streamlit UI  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- LangChain  
- Hugging Face Inference API  

---

## ⚙️ Setup

Clone the repository:

git clone https://github.com/Mohie-Aldin-Sinan/Explainify.git  
cd Explainify  

Create virtual environment & install dependencies:

python -m venv venv  
venv\Scripts\activate   (Mac/Linux: source venv/bin/activate)  
pip install -r requirements.txt  

Create a `.env` file in the project root:

HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here  

Run the app:

streamlit run app/app.py  

Open in browser:

http://localhost:8501

---

## 📜 License

MIT License
