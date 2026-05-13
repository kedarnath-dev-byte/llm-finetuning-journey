# Hugging Face Pipeline API

## Script

`src/08_hf_pipeline_api.py`

## Output Proof

`outputs/hf_pipeline_api_output.txt`

## What I Practiced

In this practical, I used Hugging Face `pipeline()` for quick model inference.

I tested:

- Sentiment analysis
- Zero-shot classification
- Text generation
- Summarization with graceful error handling
- Question answering with graceful error handling

## What Is Pipeline API?

Hugging Face `pipeline()` is a high-level API for quick inference.

It hides many internal steps:

Raw text
-> tokenizer
-> model input tensors
-> model inference
-> logits/output
-> postprocessing
-> final readable result

Pipeline is useful for fast prototyping before writing custom `AutoModel`, `Trainer`, or production inference code.

## 1. Sentiment Analysis Pipeline

Code used:

`pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")`

Output:

- Positive sentence was classified as `POSITIVE`
- Negative sentence was classified as `NEGATIVE`

Meaning:

The pipeline used a DistilBERT model already fine-tuned for sentiment classification.

## 2. Zero-Shot Classification Pipeline

Code used:

`pipeline("zero-shot-classification", model="facebook/bart-large-mnli")`

Input text:

`This tutorial explains tokenization, embeddings, and transformer models.`

Candidate labels:

- education
- politics
- business
- agriculture

Highest score:

`education`

Meaning:

Zero-shot classification can classify text into custom labels without task-specific fine-tuning.

## 3. Text Generation Pipeline

Code used:

`pipeline("text-generation", model="gpt2")`

Prompt:

`Hugging Face is useful for`

The model generated a continuation using next-token prediction.

Meaning:

GPT-style models generate text by repeatedly predicting the next token.

## 4. Summarization Pipeline Issue

The script first failed because my installed Transformers environment did not support:

`summarization`

Error:

`Unknown task summarization`

I added graceful error handling using `try/except`.

Now the script logs the issue and continues execution instead of crashing.

## 5. Question Answering Pipeline Issue

The installed pipeline registry also did not support:

`question-answering`

Error:

`Unknown task question-answering`

This was also handled with `try/except`.

## Debugging Learning

The first version of the script crashed at summarization.

I fixed it by adding exception handling around optional/version-sensitive pipeline tasks.

This is important because real production ML systems must handle library version differences and unsupported tasks gracefully.

## Why This Matters

Pipeline API is useful for:

- Fast demos
- Model exploration
- Proof of concept
- Quick business validation
- Testing pretrained models before fine-tuning

But for production and fine-tuning, we often move to:

- `AutoTokenizer`
- `AutoModel`
- `AutoModelForSequenceClassification`
- `AutoModelForCausalLM`
- `Trainer`
- custom inference code
- model serving APIs

## 2 Crore Interview Explanation

I used Hugging Face pipeline API for rapid prototyping. Sentiment analysis classified positive and negative text using a fine-tuned DistilBERT model. Zero-shot classification used BART-MNLI to classify a tutorial sentence into candidate labels without task-specific fine-tuning. Text generation used GPT-2 for next-token generation. Summarization and question-answering were unsupported in my installed Transformers pipeline registry, so I added graceful exception handling and documented the issue. This taught me that pipeline is useful for quick demos, but production systems often require AutoModel, Trainer, custom inference, and robust version handling.

## 2 Crore Interview Question

When would you use Hugging Face pipeline API, and when would you avoid it?

## Strong Answer

I would use pipeline API for fast prototyping, demos, model exploration, and proof-of-concept validation. I would avoid relying only on pipeline for production fine-tuning or scalable inference because production systems need more control over tokenization, batching, device placement, error handling, logging, latency, model versioning, and deployment. In production, I would often move to AutoTokenizer, AutoModel, Trainer, or custom inference services.

## Industry Mapping

### Education

Quickly test sentiment, topic classification, and summarization-style prototypes for student content.

### Agriculture

Prototype farmer query classification into crop disease, irrigation, soil, weather, or subsidy categories.

### Healthcare

Prototype hospital FAQ classification or patient-support routing with strict human supervision.

### Finance

Classify customer complaints, loan queries, or support tickets.

### Legal

Prototype clause classification or document topic tagging.

### HR

Classify resumes, candidate messages, or interview feedback.

### Media

Generate draft content or classify scripts/topics.

## Memory Line

Pipeline API is for fast prototyping.
AutoModel is for deeper control.
Trainer is for fine-tuning.
Custom inference is for production.
Graceful error handling makes ML code robust.
