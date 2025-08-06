# 🚀 CareerMateAI — Smart Career Insights
CareerMateAI is a simple and smart AI-powered tool that gives personalized career insights based on your uploaded resume or any career-related PDFs. It uses a powerful local LLM (LLaMA 3 via Ollama), LangChain, and FAISS for semantic search, with a clean Gradio-based UI.

🧠 Features
📄 Upload your resume or any career PDF

🤖 Ask career-related questions powered by LLaMA 3

🔍 Retrieves the most relevant content using vector embeddings (FAISS)

💡 Provides insightful, personalized answers

⚙️ Built with LangChain, Ollama, and Gradio

🛠️ Tech Stack
Frontend: Gradio

Backend: Python (LangChain, FAISS, HuggingFaceEmbeddings)

LLM: LLaMA 3 via Ollama

Vector Store: FAISS

PDF Loader: LangChain’s PyPDFLoader

⚙️ Setup Instructions
Clone the repo:

bash
Copy
Edit
git clone https://github.com/your-username/CareerMateAI.git
cd CareerMateAI
Create a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run Ollama (make sure it's installed):

bash
Copy
Edit
ollama run llama3
Run the app:

bash
Copy
Edit
python app.py
Open http://127.0.0.1:7860 in your browser.

📂 Folder Structure
graphql
Copy
Edit
CareerMateAI/
├── app.py                  # Main Gradio frontend
├── requirements.txt        # Required packages
├── pdfs/                   # Uploaded PDFs stored here
├── embeddings/             # FAISS vector store saved here
🔒 Note
This app runs locally and uses only local documents and models — no cloud upload or tracking involved.
