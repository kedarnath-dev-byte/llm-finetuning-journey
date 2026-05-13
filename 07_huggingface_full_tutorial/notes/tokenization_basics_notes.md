# Hugging Face Tokenization Basics

## Script
`src/04_hf_tokenization_basics.py`

## Output Proof
`outputs/tokenization_basics_output.txt`

## What I Practiced

I used Hugging Face `AutoTokenizer` with `bert-base-uncased` to understand how raw text becomes model-ready input for transformer models.

Flow:

Raw Text
-> Tokens
-> Token IDs
-> input_ids
-> token_type_ids
-> attention_mask
-> PyTorch tensors
-> Transformer model input

## Key Learnings

- Tokenizer converts raw text into tokens.
- Token IDs are numerical IDs from the model vocabulary.
- `input_ids` are the final token numbers passed to the model.
- `[CLS]` is added at the beginning for BERT-style models.
- `[SEP]` is added at the end or between sentence pairs.
- `token_type_ids` identify sentence A and sentence B.
- `attention_mask` tells the model real tokens vs padding tokens.
- Padding makes batch sentences equal length.
- Truncation cuts long text to fit max sequence length.
- Batch tokenization prepares multiple sentences for model training or inference.

## 2 Crore Interview Explanation

I implemented Hugging Face tokenization using BERT's `AutoTokenizer`. I converted raw text into tokens, token IDs, model-ready `input_ids`, `token_type_ids`, and `attention_mask`. I also practiced padding, truncation, and batch tokenization. This helped me understand how raw language becomes tensor input for transformer models before inference or fine-tuning.

## Senior-Level Notes

- Tokenizer must match the pretrained model.
- Wrong tokenizer can create wrong token IDs.
- Padding is needed for batching.
- Attention mask prevents the model from attending to padding.
- Truncation can remove important context.
- Sequence length affects memory, speed, and cost.

## 2 Crore Interview Question

How would you design a tokenization strategy for a production fine-tuning system where customer documents have highly variable lengths?

## Strong Answer

I would first analyze the document length distribution. Then I would choose max sequence length based on memory, latency, and information retention. For long documents, I would use chunking, sliding windows, summarization, retrieval-based preprocessing, or long-context models instead of blindly truncating.

## Memory Line

Tokenizer converts human language into model-readable numbers.
Attention mask tells the model what to read and what to ignore.
Padding gives equal shape.
Truncation controls length.
Batch tokenization prepares data for training.
