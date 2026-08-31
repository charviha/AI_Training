# AI RAG Assistant

An AI-powered Retrieval-Augmented Generation (RAG) application that uses semantic search to retrieve relevant information and generate answers using a Large Language Model.

## Features

- Retrieval-Augmented Generation (RAG)
- Semantic search using Sentence Transformers
- FAISS vector similarity search
- Google Gemini for answer generation
- Conversation memory
- Tool-based agent functionality
- Local document/data retrieval

## Technologies Used

- Python
- Google GenAI
- Sentence Transformers
- FAISS
- NumPy
- PyTorch
- Transformers

## Project Structure

```text
day_3_AI_assignment/
│
├── agent.py              # Agent functionality
├── main.py               # Main application
├── memory.py             # Conversation memory
├── memory.json           # Stored memory
├── rag.py                # RAG and semantic search functionality
├── tools.py              # Supporting tools
├── data/                 # Application data
├── screenshots/          # Application screenshots
├── requirements.txt      # Python dependencies
├── .gitignore            # Git ignored files
└── README.md             # Project documentation
