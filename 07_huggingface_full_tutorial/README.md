# Hugging Face Full Tutorial

## Module Goal

This module is part of my LLM Fine-Tuning Journey.

The goal of this module is to understand and implement the Hugging Face ecosystem hands-on, including datasets, tokenization, custom tokenizer training, embeddings, AutoModel classes, task-specific heads, and pipeline-based inference.

This module is not only theory. It contains real Python scripts, execution outputs, generated charts, tokenizer artifacts, and debugging notes.

---

## Why Hugging Face Matters

Hugging Face is one of the most important ecosystems for modern AI/ML/GenAI development.

It provides:

- Pretrained models
- Datasets
- Tokenizers
- Transformers library
- Evaluation tools
- Hub API
- Inference tools
- Model and dataset sharing
- Fine-tuning support
- Deployment options through Spaces and APIs

For LLM fine-tuning, Hugging Face is important because it helps with:

- Loading datasets
- Preparing text
- Tokenizing data
- Loading pretrained models
- Fine-tuning models
- Evaluating models
- Saving and sharing artifacts

---

## Hands-On Scripts Completed

| No. | Script | Purpose |
|---|---|---|
| 1 | `src/01_hf_environment_check.py` | Validate Python, PyTorch, Hugging Face libraries, and CUDA availability |
| 2 | `src/02_hf_dataset_loading_preprocessing.py` | Load IMDb dataset, inspect splits, shuffle, select, filter, and map |
| 3 | `src/03_dataset_visualization_analysis.py` | Perform EDA with label distribution, word count distribution, and common word analysis |
| 4 | `src/04_hf_tokenization_basics.py` | Practice tokenizer, tokens, token IDs, input IDs, token type IDs, attention mask, padding, truncation, and batch tokenization |
| 5 | `src/05_train_custom_bpe_tokenizer.py` | Train a custom BPE tokenizer and save tokenizer artifacts |
| 6 | `src/06_embeddings_and_similarity.py` | Generate embeddings using AutoModel and SentenceTransformer, then compare cosine similarity |
| 7 | `src/07_automodel_classes_and_heads.py` | Understand AutoModel, sequence classification head, causal LM head, and AutoConfig |
| 8 | `src/08_hf_pipeline_api.py` | Practice pipeline API for sentiment analysis, zero-shot classification, text generation, and graceful error handling |

---

## Output Proofs

| Output File | What It Proves |
|---|---|
| `outputs/environment_check_output.txt` | Environment was validated |
| `outputs/dataset_loading_preprocessing_output.txt` | IMDb dataset was loaded and preprocessed |
| `outputs/dataset_visualization_analysis_output.txt` | EDA summary was generated |
| `outputs/tokenization_basics_output.txt` | Tokenization workflow was executed |
| `outputs/custom_bpe_tokenizer_output.txt` | Custom BPE tokenizer was trained |
| `outputs/embeddings_and_similarity_output.txt` | Embedding similarity was calculated |
| `outputs/automodel_classes_and_heads_output.txt` | AutoModel class experiments were executed |
| `outputs/hf_pipeline_api_output.txt` | Pipeline API experiments were executed |

---

## Generated Artifacts

### Dataset EDA Charts

- `outputs/imdb_label_distribution.png`
- `outputs/imdb_word_count_distribution.png`
- `outputs/imdb_top_common_words.png`

### Custom Tokenizer Artifacts

- `outputs/custom_bpe_tokenizer/custom_tokenizer.json`
- `outputs/custom_bpe_tokenizer/hf_fast_tokenizer/`

These artifacts prove that I trained and saved a custom tokenizer.

---

## Notes Created

| Note File | Concept |
|---|---|
| `notes/tokenization_basics_notes.md` | Tokenization basics |
| `notes/custom_bpe_tokenizer_notes.md` | Custom BPE tokenizer training |
| `notes/embeddings_and_similarity_notes.md` | Embeddings and cosine similarity |
| `notes/automodel_classes_and_heads_notes.md` | AutoModel classes and task-specific heads |
| `notes/hf_pipeline_api_notes.md` | Hugging Face pipeline API and debugging |

---

## Key Concepts Learned

### 1. Environment Validation

Before coding, I verified:

- Python version
- PyTorch installation
- CPU/GPU availability
- Hugging Face libraries
- Dataset/evaluation/visualization dependencies

My local setup uses CPU-only PyTorch, which is suitable for lightweight Hugging Face experiments. Heavy fine-tuning should be moved to Colab, Kaggle, or cloud GPU.

---

### 2. Hugging Face Datasets

I practiced:

- `load_dataset("imdb")`
- `DatasetDict`
- train/test/unsupervised splits
- `shuffle(seed=42)`
- `select(range(...))`
- `filter()`
- `map()`

This helped me understand dataset preparation before tokenization and fine-tuning.

---

### 3. Dataset Visualization

I performed EDA using:

- pandas
- matplotlib
- Counter
- regex cleaning

I generated charts for:

- label distribution
- review word count distribution
- top common words

This helps understand data balance, sequence length, and preprocessing needs.

---

### 4. Tokenization

I practiced:

- `AutoTokenizer.from_pretrained("bert-base-uncased")`
- `tokenizer.tokenize()`
- `convert_tokens_to_ids()`
- `input_ids`
- `token_type_ids`
- `attention_mask`
- padding
- truncation
- batch tokenization

Important learning:

Raw text must become model-readable numbers before entering a transformer model.

---

### 5. Custom BPE Tokenizer

I trained a custom tokenizer using:

- `Tokenizer`
- `BPE`
- `Whitespace`
- `BpeTrainer`
- `PreTrainedTokenizerFast`

Important learning:

Tokenizer quality depends on corpus size, domain coverage, vocabulary size, and tokenizer algorithm.

For most fine-tuning projects, the original pretrained model tokenizer should be reused unless domain/language mismatch is severe.

---

### 6. Embeddings and Similarity

I implemented embeddings using:

- `AutoTokenizer`
- `AutoModel`
- attention-mask-aware mean pooling
- `SentenceTransformer`
- `cosine_similarity`

Important learning:

Embeddings convert meaning into vectors. They are the foundation for RAG, semantic search, recommendations, clustering, and document similarity.

---

### 7. AutoModel Classes and Heads

I practiced:

- `AutoModel`
- `AutoModelForSequenceClassification`
- `AutoModelForCausalLM`
- `AutoConfig`

Important learning:

Choosing the correct model class is critical.

- `AutoModel` gives hidden states
- `AutoModelForSequenceClassification` gives class logits
- `AutoModelForCausalLM` generates text
- `AutoConfig` inspects and modifies architecture settings

---

### 8. Pipeline API

I practiced:

- sentiment analysis
- zero-shot classification
- text generation
- graceful error handling for unsupported tasks

Important learning:

Pipeline API is useful for rapid prototyping, but production/fine-tuning systems usually need more control through AutoTokenizer, AutoModel, Trainer, or custom inference code.

---

## Debugging Lessons

### Hugging Face Symlink Warning on Windows

I encountered Hugging Face cache symlink warnings on Windows.

Meaning:

- Not a runtime failure
- Cache still works
- Disk usage may be less optimized
- Developer Mode or administrator mode can improve symlink support

### Unauthenticated Hugging Face Requests

I encountered warnings about unauthenticated HF Hub requests.

Meaning:

- Public downloads still work
- Login/token is needed for higher rate limits, private models, uploads, and Hub write operations

### Unsupported Pipeline Tasks

My installed Transformers environment did not support:

- `summarization`
- `question-answering`

I handled this using `try/except` so the script continued and documented the issue.

---

## Learning Level

I now understand:

- How Hugging Face loads datasets
- How data is preprocessed before fine-tuning
- How tokenization converts text into model inputs
- How custom tokenizers are trained
- How embeddings are generated
- How cosine similarity works
- How AutoModel classes differ
- How pipeline API works for fast prototyping

---

## Job Level

This module helps prepare for AI/GenAI roles involving:

- Hugging Face Transformers
- NLP preprocessing
- LLM fine-tuning foundations
- RAG systems
- semantic search
- model inference
- model evaluation
- production debugging

---

## Business Level

These concepts can be used to build AI solutions for:

- Education: student doubt matching, personalized tutors
- Agriculture: farmer query search, crop advisory retrieval
- Healthcare: FAQ routing and patient-support assistants with human supervision
- Finance: customer-support classification and document search
- Legal: contract clause retrieval and document classification
- HR: resume-job matching and candidate classification
- Media: content generation and topic classification

---

## 2 Crore Interview Explanation

In this Hugging Face module, I built a hands-on codebase covering the early LLM engineering workflow. I validated my environment, loaded and preprocessed the IMDb dataset, performed EDA with visualizations, practiced tokenization, trained a custom BPE tokenizer, generated embeddings with AutoModel and SentenceTransformer, compared semantic similarity using cosine similarity, explored AutoModel classes and task-specific heads, and used the pipeline API for rapid prototyping. I also debugged real environment issues like unsupported pipeline tasks and added graceful error handling. This gave me practical understanding of how Hugging Face supports dataset handling, tokenization, embeddings, model inference, task heads, and production-style experimentation.

---

## Memory Line

Environment validates setup.

Datasets prepare data.

EDA understands data.

Tokenizer converts text to IDs.

Custom tokenizer learns vocabulary.

Embeddings capture meaning.

AutoModel classes choose task behavior.

Pipeline API gives quick prototypes.

Debugging makes the code production-aware.
