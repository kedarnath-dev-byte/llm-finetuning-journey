# Hugging Face AutoModel Classes and Task-Specific Heads

## Script

`src/07_automodel_classes_and_heads.py`

## Output Proof

`outputs/automodel_classes_and_heads_output.txt`

## What I Practiced

In this practical, I learned how different Hugging Face AutoModel classes are used for different tasks.

I practiced:

- `AutoModel`
- `AutoModelForSequenceClassification`
- `AutoModelForCausalLM`
- `AutoConfig`

## Big Idea

The same transformer backbone can be used for different tasks by attaching different heads.

Base Transformer
-> hidden states / embeddings

Base Transformer + Classification Head
-> class logits / sentiment / intent / topic

Decoder Model + Language Modeling Head
-> next-token prediction / text generation

Config
-> architecture metadata and task settings

## 1. AutoModel

`AutoModel` loads the base transformer model without a task-specific head.

It gives hidden states.

Example output:

`last_hidden_state shape: (1, 11, 768)`

Meaning:

- `1` = batch size
- `11` = number of tokens
- `768` = hidden size of BERT-base

Use cases:

- Embeddings
- Feature extraction
- Semantic representation
- Custom heads
- RAG embedding experiments

## 2. AutoModelForSequenceClassification

`AutoModelForSequenceClassification` loads a base transformer with a classification head.

In my script, I used:

`distilbert-base-uncased-finetuned-sst-2-english`

The model predicted:

`POSITIVE`

for:

`I really enjoyed learning Hugging Face today.`

It produced:

- logits
- probabilities
- predicted class id
- predicted label

Use cases:

- Sentiment analysis
- Intent classification
- Spam detection
- Topic classification
- Support ticket routing
- Resume category classification

## 3. AutoModelForCausalLM

`AutoModelForCausalLM` is used for decoder-style next-token prediction and text generation.

In my script, I used:

`gpt2`

Prompt:

`Hugging Face is useful for`

Generated continuation:

`Hugging Face is useful for a lot of reasons...`

Use cases:

- Text generation
- Chat-style generation
- Completion systems
- Story generation
- Code generation basics
- LLM fine-tuning preparation

## 4. AutoConfig

`AutoConfig` loads model architecture metadata.

For `bert-base-uncased`, I inspected:

- model type
- hidden size
- number of hidden layers
- number of attention heads
- vocabulary size

Example:

- hidden size = 768
- hidden layers = 12
- attention heads = 12
- vocabulary size = 30522

I also changed:

`num_labels = 5`

This simulates preparing a model for a custom 5-class classification task.

## Why This Matters

Choosing the correct Hugging Face model class is critical.

Wrong class can cause:

- wrong output type
- shape mismatch
- missing logits
- unsuitable model behavior
- incorrect task implementation

## Production Learning

Use `AutoModel` when you need hidden states or embeddings.

Use `AutoModelForSequenceClassification` when you need class prediction.

Use `AutoModelForCausalLM` when you need next-token generation.

Use `AutoConfig` when you need to inspect or modify model architecture settings.

## 2 Crore Interview Explanation

I implemented multiple Hugging Face AutoModel classes to understand model heads. `AutoModel` gave me base transformer hidden states with shape `(batch, tokens, hidden_size)`. `AutoModelForSequenceClassification` added a classification head and produced logits, probabilities, and a sentiment label. `AutoModelForCausalLM` loaded GPT-2 with a language modeling head and generated text through next-token prediction. `AutoConfig` helped me inspect BERT architecture parameters like hidden size, layers, attention heads, vocabulary size, and modify `num_labels` for custom classification. This taught me that choosing the correct model class is critical for correct output behavior.

## 2 Crore Interview Question

How do you decide which Hugging Face AutoModel class to use for a business problem?

## Strong Answer

I first identify the task. If I need embeddings or hidden states, I use `AutoModel`. If I need classification, I use `AutoModelForSequenceClassification`. If I need text generation or next-token prediction, I use `AutoModelForCausalLM`. If I need to inspect or customize architecture settings such as number of labels, hidden size, vocabulary size, or attention heads, I use `AutoConfig`. The correct class depends on the output required by the business problem.

## Industry Mapping

### Education

Use sequence classification to classify student doubts by subject or difficulty.

### Agriculture

Use classification to categorize farmer issues like crop disease, irrigation, soil, or subsidy.

### Healthcare

Use classification for hospital FAQ routing, with human supervision.

### Finance

Use classification for customer intent, complaint routing, or risk document tagging.

### Legal

Use classification for contract clause type detection.

### HR

Use classification for resume category, role matching, or candidate stage.

### Media

Use causal language models for content generation and script drafting.

## Memory Line

AutoModel gives hidden states.
SequenceClassification gives class logits.
CausalLM generates next tokens.
AutoConfig shows model architecture.
Correct class = correct task output.
