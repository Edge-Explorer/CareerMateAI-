import os
import shutil
import gradio as gr

from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.llms import Ollama
from langchain_community.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA

# Directories
PDF_DIR = "pdfs"
DB_DIR = "embeddings/career_db"

os.makedirs(PDF_DIR, exist_ok=True)
os.makedirs("embeddings", exist_ok=True)

# Upload PDF and rebuild vector DB
def upload_pdf(file_path):
    try:
        filename = os.path.basename(file_path)
        save_path = os.path.join(PDF_DIR, filename)
        shutil.copy(file_path, save_path)

        loader = PyPDFLoader(save_path)
        pages = loader.load()

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        db = FAISS.from_documents(pages, embeddings)
        db.save_local(DB_DIR)

        return "✅ PDF uploaded and DB rebuilt successfully!"
    except Exception as e:
        print("[UPLOAD ERROR]:", str(e))
        return f"❌ Upload failed: {str(e)}"

# Answer questions using RetrievalQA
def get_answer(query):
    try:
        if not os.path.exists(DB_DIR):
            return "⚠️ Please upload a resume PDF first."

        embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
        db = FAISS.load_local(DB_DIR, embeddings, allow_dangerous_deserialization=True)

        llm = Ollama(model="llama3")
        qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=db.as_retriever())

        return qa_chain.run(query)
    except Exception as e:
        print("[ANSWER ERROR]:", str(e))
        return f"❌ Error: {str(e)}"

# Gradio UI
with gr.Blocks(theme=gr.themes.Base()) as demo:
    gr.Markdown("🚀 **CareerMateAI — Smart Career Insights from Your Resume**")

    with gr.Row():
        with gr.Column(scale=3):
            question = gr.Textbox(label="💬 Ask your career question")
            answer = gr.Textbox(label="🧠 CareerMateAI Answer", interactive=False)
            ask_btn = gr.Button("Get Answer")

        with gr.Column(scale=2):
            file_input = gr.File(label="📄 Upload Resume (PDF)", file_types=[".pdf"], type="filepath")
            status = gr.Textbox(label="📌 Upload Status", interactive=False)
            upload_btn = gr.Button("Upload & Rebuild DB")

    upload_btn.click(fn=upload_pdf, inputs=[file_input], outputs=[status])
    ask_btn.click(fn=get_answer, inputs=[question], outputs=[answer])

demo.launch()
