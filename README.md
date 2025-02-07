# Agentic_AI_CrewAI_chatbot
This repository contains an Agentic AI Chatbot that processes PDF documents and answers questions based on their content. It uses CrewAI, Ollama, and PDFSearchTool to extract relevant information and provide accurate responses.
Features:
✅ Autonomous AI Agents for document analysis
✅ Ollama’s LLM (gemma2) for answering questions
✅ Uses CrewAI to organize and run agents
✅ PDF-based retrieval with PDFSearchTool
✅ Fully customizable AI crew and task setup

📄 README.md
Create a README.md file and paste the following content:

md
Copy
Edit
# 🤖 Agentic_AI_CrewAI_chatbot for PDFs

This project is an **AI-powered chatbot** that allows users to **ask questions based on PDF content**. It uses **CrewAI**, **Ollama**, and **PDFSearchTool** to extract relevant information and generate responses.

---

## 🚀 Features
✅ **Autonomous AI Agents** - Uses CrewAI for intelligent task execution  
✅ **PDF Processing** - Extracts relevant answers from PDFs  
✅ **Ollama’s `gemma2` Model** - Provides high-quality responses  
✅ **Customizable AI Crew** - Easily modify agents, tasks, and crew setup  

---

## 🛠️ Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yashrj1310/Agentic_Ai_Chatbot.git
cd Agentic_Ai_Chatbot
2️⃣ Install Dependencies
sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Ollama Server
Make sure you have Ollama running locally:

sh
Copy
Edit
ollama serve
4️⃣ Run the Chatbot
sh
Copy
Edit
python app.py
📌 How It Works
1️⃣ Place your PDF file inside the data/ folder
2️⃣ The AI agent processes the PDF and indexes its content
3️⃣ User asks a question, and the chatbot retrieves the answer
4️⃣ Ollama’s LLM (gemma2) provides the response

📄 Example Query
python
Copy
Edit
customer_question = "What is the definition of Transformer?"
results = crew.kickoff({"customer_question": customer_question})
print(results)
🤝 Contributing
Feel free to fork this repository, create a new branch, and submit a pull request.
