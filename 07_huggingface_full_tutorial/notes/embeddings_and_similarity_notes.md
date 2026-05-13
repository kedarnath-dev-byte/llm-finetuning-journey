# Embeddings and Cosine Similarity

## Script

`src/06_embeddings_and_similarity.py`

## Output Proof

`outputs/embeddings_and_similarity_output.txt`

## What I Practiced

In this practical, I generated sentence embeddings using two approaches:

1. Hugging Face `AutoModel` with mean pooling
2. `SentenceTransformer` model for direct sentence embeddings

I then compared sentence meaning using cosine similarity.

## Flow

Raw Text
-> Tokenizer
-> input_ids and attention_mask
-> Transformer model
-> token-level embeddings
-> mean pooling
-> sentence embedding
-> cosine similarity

## Key Concepts

### Embedding

An embedding is a numerical vector representation of text.

It converts meaning into numbers.

Example:

Two similar sentences should have vectors close to each other.

Two unrelated sentences should have vectors farther apart.

### AutoModel Embeddings

`AutoModel` loads the base transformer model without a task-specific head.

It gives token-level hidden states.

Because it gives token-level vectors, we need pooling to create one sentence vector.

### Mean Pooling

Mean pooling averages token embeddings to create one sentence embedding.

Important:

Mean pooling should use the attention mask so padding tokens do not affect the final sentence embedding.

### Cosine Similarity

Cosine similarity compares the direction of two vectors.

Higher similarity means the sentence meanings are closer.

Lower or negative similarity means the meanings are different.

### SentenceTransformer

Sentence Transformers are models trained specifically to create sentence embeddings.

They are easier and often better for semantic search, RAG, and similarity tasks than raw AutoModel outputs.

## My Output

Sentence 1:

`Hugging Face helps developers build AI applications.`

Sentence 2:

`Hugging Face provides tools for machine learning developers.`

Sentence 3:

`The farmer is checking crop disease in the field.`

Using SentenceTransformer:

`Similarity(sentence_1, sentence_2): 0.8332`

`Similarity(sentence_1, sentence_3): -0.0740`

## Interpretation

Sentence 1 and Sentence 2 are both about Hugging Face, AI tools, and developers, so similarity is high.

Sentence 3 is about agriculture and crop disease, so it is not semantically close to Sentence 1.

## Why This Matters

Embeddings are the foundation of:

- RAG
- Semantic search
- Document similarity
- Recommendation systems
- Clustering
- Resume-job matching
- Customer support ticket routing
- Duplicate question detection
- Knowledge base search

## Industry Use Cases

### Education

Match student doubts with relevant explanations, notes, or video lessons.

### Agriculture

Match farmer questions with crop disease documents, soil guidance, or government schemes.

### Healthcare

Retrieve relevant hospital FAQs or medical education documents with human supervision.

### Finance

Match customer queries with policy documents, reports, or compliance FAQs.

### Legal

Retrieve relevant clauses from contracts or case-law documents.

### HR

Match resumes with job descriptions using semantic similarity.

## 2 Crore Interview Explanation

I implemented embeddings in two ways. First, I used BERT `AutoModel` to extract token-level hidden states and applied attention-mask-aware mean pooling to create sentence embeddings. Then I calculated cosine similarity between sentence vectors. Second, I used `sentence-transformers/all-MiniLM-L6-v2`, which directly produces sentence embeddings optimized for semantic similarity. This helped me understand the difference between raw transformer representations and retrieval-ready embeddings used in RAG and semantic search systems.

## 2 Crore Interview Question

How would you design an embedding-based semantic search system for enterprise documents?

## Strong Answer

I would first collect and clean the documents, split them into meaningful chunks, generate embeddings using a strong sentence embedding model, store those embeddings in a vector database, and retrieve top matching chunks using cosine similarity or approximate nearest neighbor search. I would evaluate retrieval quality using human-labeled queries, measure precision and recall, handle access control, update embeddings when documents change, and combine retrieval with an LLM for grounded RAG answers.

## Memory Line

Tokenization converts text into IDs.
Transformer converts IDs into hidden states.
Pooling converts token vectors into sentence vectors.
Cosine similarity compares meanings.
Sentence Transformers make semantic search easier.
Embeddings power RAG.
