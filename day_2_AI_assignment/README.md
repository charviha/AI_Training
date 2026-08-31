# Day 2 – FAISS Semantic Search

## Objective

Build a mini semantic search engine in Python using **Sentence Transformers** and **FAISS**.

The project demonstrates how text can be converted into embeddings, stored in a vector index, and searched using semantic similarity.

## Technologies Used

* Python
* Sentence Transformers
* `all-MiniLM-L6-v2`
* FAISS
* NumPy
* Jupyter Notebook

## Project Structure

```text
day_2_AI_assignment/
│
├── semantic_search.ipynb
├── semantic_search.py
├── theory_answers.md
├── README.md
└── .gitignore
```

## Tasks Completed

### Task 1 – Embedding Generation

* Created a knowledge base containing support-related sentences.
* Loaded the `all-MiniLM-L6-v2` embedding model.
* Generated embeddings for the knowledge base.
* Each sentence is converted into a **384-dimensional vector**.

Example:

```python
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(knowledge_base)
```

Expected embedding shape when using 10 sentences:

```text
(10, 384)
```

### Task 2 – FAISS Index

Created a FAISS `IndexFlatL2` index:

```python
index = faiss.IndexFlatL2(384)
```

The embeddings are normalized before adding them to the index:

```python
faiss.normalize_L2(embeddings)
```

The vectors are then stored using:

```python
index.add(embeddings)
```

The number of stored vectors can be checked using:

```python
index.ntotal
```

### Task 3 – Semantic Search

A user query is converted into an embedding and normalized before searching.

```python
query_embedding = model.encode([query])
faiss.normalize_L2(query_embedding)

distances, indices = index.search(query_embedding, k=3)
```

The system returns the **Top 3 most relevant sentences**.

Example queries:

* "I forgot my password. How can I reset it?"
* "I was charged twice for the same payment."
* "Why can't I log into my account?"

### Task 4 – Interactive CLI

The project includes an interactive command-line interface.

Users can continuously enter queries:

```text
Enter your query: I forgot my password
```

The system returns the Top 3 matching sentences.

To exit:

```text
exit
```

## Semantic Search Workflow

```text
Knowledge Base
       ↓
Sentence Transformer
       ↓
384-D Embeddings
       ↓
Normalize Embeddings
       ↓
FAISS Index
       ↓
User Query
       ↓
Query Embedding
       ↓
Normalize Query
       ↓
FAISS Similarity Search
       ↓
Top 3 Results
```

## Example Knowledge Base Topics

The knowledge base contains information related to:

* Password reset
* Login issues
* Account management
* Billing
* Payment methods
* Account recovery
* Account security
* Subscription management

## FAISS Scoring

This project uses:

```python
faiss.IndexFlatL2(384)
```

Therefore, the search returns **L2 distance**.

A **smaller distance means a better match**.

For example:

```text
Rank    Score    Matched Sentence
1       0.12     To reset your password...
2       0.58     A password reset link will be sent...
3       0.93     If you cannot log in...
```

## Theory

The theoretical questions related to:

1. `IndexFlatL2` vs `IndexFlatIP`
2. Embedding normalization and cosine similarity
3. Approximate Nearest Neighbour (ANN) search

are answered in:

```text
theory_answers.md
```

## How to Run

Activate the virtual environment:

```bash
source rag_venv/bin/activate
```

Run the Python implementation:

```bash
python semantic_search.py
```

Alternatively, open and run:

```text
semantic_search.ipynb
```

in Jupyter Notebook.

## Learning Outcome

This assignment demonstrates the basic retrieval component used in **Retrieval-Augmented Generation (RAG)** systems.

It covers:

* Text embeddings
* Vector representations
* Normalization
* Vector databases/indexes
* Semantic similarity
* Top-K retrieval
* FAISS search
* Interactive semantic search

