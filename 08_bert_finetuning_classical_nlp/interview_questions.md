# Interview Questions: BERT Fine-Tuning

## 10 LPA Level

### 1. What is BERT?

BERT is an encoder-based Transformer model used mainly for language understanding tasks like classification, NER, QA, and embeddings.

### 2. Is BERT a generative model?

No. BERT is not a generative model. It is mainly used for understanding tasks.

### 3. What is tokenization?

Tokenization converts raw text into tokens and token IDs that a model can process.

### 4. What is IMDb dataset used for here?

IMDb is used for binary sentiment classification.

- 0 = negative
- 1 = positive

### 5. What is fine-tuning?

Fine-tuning means adapting a pretrained model to a specific supervised task using labeled data.

---

## 50 LPA Level

### 1. Why do we use `BertForSequenceClassification`?

Because IMDb sentiment analysis is a sequence-level classification task. This class adds a classification head on top of BERT.

### 2. Why do we use padding and truncation?

Padding makes all sequences the same length. Truncation cuts sequences longer than the maximum length.

### 3. Why does Trainer expect `labels`?

Hugging Face Trainer expects the target column to be named `labels` so it can automatically compute supervised training loss.

### 4. Why should tokenizer and model come from the same checkpoint?

Because the model was pretrained with that tokenizer vocabulary and tokenization rules. A mismatch can create wrong token IDs.

### 5. Why is a small learning rate used?

BERT is already pretrained. A small learning rate helps adapt it without destroying pretrained knowledge.

---

## 1 Crore Level

### 1. What happens when loading `BertForSequenceClassification` from `bert-base-uncased`?

The original MLM/NSP heads are ignored, and a new classification head is initialized for the downstream classification task.

### 2. What is the difference between BERT and GPT?

BERT is encoder-only and good for understanding. GPT is decoder-only and good for generation.

### 3. What is the role of attention mask?

Attention mask tells the model which tokens are real and which tokens are padding.

### 4. What are task-specific heads?

Task-specific heads are layers added on top of BERT for specific outputs like classification labels, token labels, or QA spans.

### 5. Why evaluate on test data?

To check whether the model generalizes to unseen examples instead of only memorizing training data.

---

## 1.5 Crore Level

### 1. When would you use BERT instead of a large LLM?

Use BERT when the task is classification, NER, QA extraction, embeddings, or low-latency understanding where long-form generation is not needed.

### 2. Full fine-tuning vs freezing layers — how do you decide?

Full fine-tuning is useful when we have enough data and GPU. Freezing layers is useful when data or compute is limited and we want faster training.

### 3. How would you productionize this model?

Steps:

1. Save model and tokenizer.
2. Create inference API.
3. Add validation and logging.
4. Monitor prediction quality.
5. Version model artifacts.
6. Protect private data.
7. Retrain when performance drops.

### 4. What can go wrong in BERT fine-tuning?

Common issues:

- Wrong label format
- Tokenizer/model mismatch
- Overfitting
- Too high learning rate
- Too small or biased dataset
- GPU memory issues
- Poor evaluation setup

### 5. How does BERT help in RAG?

BERT-style models can generate embeddings or rerank retrieved passages. However, SentenceTransformer-style models are usually preferred for sentence embeddings.

---

## 2 Crore Level

### 1. How would you choose between BERT, RAG, and LLM agents?

- BERT: fixed supervised understanding tasks
- RAG: knowledge-grounded answering from documents
- LLM agents: tool use, workflows, multi-step decisions
- Hybrid: enterprise systems combining classifier, retriever, generator, and agent tools

### 2. How would you build a BERT-based enterprise NLP platform?

I would build reusable pipelines for:

- Data ingestion
- Label validation
- Tokenization
- Fine-tuning
- Evaluation
- Model registry
- Inference API
- Monitoring
- Human review
- Retraining

### 3. What are the cost advantages of BERT?

BERT is smaller and cheaper than large generative models for classification and extraction tasks. It can reduce inference cost and latency.

### 4. What privacy precautions are needed?

- Remove PII
- Avoid pushing private models publicly
- Use private repositories for sensitive models
- Track dataset consent
- Add access control
- Log predictions safely
- Use human review in healthcare/legal domains

### 5. How would you explain this project to a senior AI engineer?

I fine-tuned `bert-base-uncased` on IMDb sentiment classification using Colab T4 GPU and Hugging Face Trainer. I sampled 1000 training rows and 500 test rows, tokenized with max length 256, used `BertForSequenceClassification`, trained for 1 epoch with learning rate 2e-5, evaluated loss, saved model/tokenizer, reloaded with pipeline, and validated inference on new reviews. I also documented task-specific heads for classification, NER, and QA.

---

## Final Interview Memory Line

BERT is an encoder-based language understanding model. Fine-tuning adapts its pretrained representations to supervised business tasks through task-specific heads.
