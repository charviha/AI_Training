# Task 5 – FAISS Semantic Search Theory Answers

## Q1. What is the difference between IndexFlatL2 and IndexFlatIP in FAISS? When would you use each?

`IndexFlatL2` and `IndexFlatIP` are two FAISS indexes that use different methods to measure similarity between vectors.

### IndexFlatL2

`IndexFlatL2` uses **L2 (Euclidean) distance**.

It measures the distance between two vectors. A **smaller distance means the vectors are more similar**.

Example:

```python
index = faiss.IndexFlatL2(384)
```

Use `IndexFlatL2` when you want to compare vectors using Euclidean distance.

### IndexFlatIP

`IndexFlatIP` uses **Inner Product (IP)** to compare vectors.

A **higher inner-product score means the vectors are more similar**.

Example:

```python
index = faiss.IndexFlatIP(384)
```

When the embeddings are normalized, inner product is equivalent to cosine similarity. Therefore, `IndexFlatIP` is commonly used when cosine similarity is required.

### Difference

| Index         | Similarity Method     | Better Match  |
| ------------- | --------------------- | ------------- |
| `IndexFlatL2` | Euclidean/L2 distance | Smaller value |
| `IndexFlatIP` | Inner Product         | Larger value  |

For this assignment, `IndexFlatL2` is used as specified in the task.

## Q2. Why do we normalise embeddings before adding to FAISS when we want cosine similarity?

Cosine similarity measures the **angle/direction between two vectors**, rather than their length.

Before adding embeddings to FAISS, we normalize them so that each vector has a magnitude of 1.

```python
faiss.normalize_L2(embeddings)
```

We also normalize the query vector:

```python
faiss.normalize_L2(query_vector)
```

When both vectors are normalized, their L2 distance and cosine similarity are mathematically related. This allows us to use normalized vectors with an L2 index to get the same ranking behavior as cosine similarity.

Therefore, normalization makes the similarity comparison focus on the **direction of the vectors rather than their magnitude**.

## Q3. FAISS uses ANN (Approximate Nearest Neighbour) search. What does "approximate" mean here and why is it acceptable?

Approximate Nearest Neighbour (ANN) search means finding vectors that are **very close to the query vector without necessarily checking every vector in the database**.

With an exact search, the system could compare the query with every stored vector:

```text
Query
  ↓
Vector 1
Vector 2
Vector 3
...
Vector 1,000,000
```

This can become slow when the database contains millions or billions of vectors.

ANN methods reduce the amount of searching required by quickly identifying promising candidates.

The result may not always be the mathematically exact nearest vector, but it is usually a very good match.

ANN is acceptable because it provides:

* Much faster search
* Better scalability for large datasets
* Lower computational cost
* Highly relevant results in most practical applications

In real-world RAG systems, the small possibility of missing the absolute closest vector is often acceptable because the improvement in search speed and scalability is much more valuable.

## Conclusion

FAISS is used to efficiently search through vector embeddings.

The semantic search process is:

```text
Text
  ↓
Embedding Model
  ↓
Vector Embeddings
  ↓
Normalization
  ↓
FAISS Index
  ↓
User Query
  ↓
Query Embedding
  ↓
Similarity Search
  ↓
Top-K Relevant Results
```

This retrieval process forms an important part of a **Retrieval-Augmented Generation (RAG)** system.

