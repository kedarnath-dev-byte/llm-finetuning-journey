# Custom BPE Tokenizer Training

## Script

`src/05_train_custom_bpe_tokenizer.py`

## Output Proof

`outputs/custom_bpe_tokenizer_output.txt`

## Tokenizer Artifacts

`outputs/custom_bpe_tokenizer/custom_tokenizer.json`

`outputs/custom_bpe_tokenizer/hf_fast_tokenizer/`

## What I Practiced

In this practical, I trained a small custom Byte Pair Encoding tokenizer using Hugging Face Tokenizers.

I practiced:

- Creating a small domain-style corpus
- Training a BPE tokenizer
- Using whitespace pre-tokenization
- Adding special tokens
- Saving tokenizer JSON
- Loading it back as a Hugging Face fast tokenizer
- Testing tokenization on unseen sentences
- Understanding `[UNK]`, input IDs, attention mask, and vocabulary size

## Why This Matters

Tokenization controls how raw text becomes model-readable input.

A tokenizer decides:

- How words are split
- Which subwords are learned
- How unknown words are handled
- How long the final token sequence becomes
- How efficiently a model can process domain-specific text

## BPE Meaning

BPE means Byte Pair Encoding.

It learns frequent character or subword combinations from the training corpus.

Small example idea:

`tokenization`

may become:

`token` + `ization`

or smaller pieces depending on the vocabulary learned.

## What My Output Taught Me

My tokenizer was trained on only 11 corpus lines.

Because the corpus was small, some words were split into many pieces.

Example:

`Fine tuning helps adapt models for education AI.`

was split into small subword tokens.

For unknown domain words, `[UNK]` appeared.

This taught me that tokenizer quality depends on:

- Corpus size
- Corpus quality
- Domain coverage
- Vocabulary size
- Tokenizer algorithm

## Important Senior-Level Point

For normal fine-tuning of an existing pretrained model, we usually reuse the original tokenizer.

Why?

Because the pretrained model's embedding layer is aligned with its original tokenizer vocabulary.

If we replace the tokenizer, we may need to:

- Resize token embeddings
- Initialize new embeddings
- Continue pretraining
- Evaluate carefully

So custom tokenizer training is powerful, but it should not be done casually.

## 2 Crore Interview Explanation

I trained a custom BPE tokenizer using Hugging Face Tokenizers. I created a small domain-style corpus, configured BPE with special tokens, used whitespace pre-tokenization, trained the tokenizer, saved it as JSON, loaded it back as a Hugging Face fast tokenizer, and tested it on unseen sentences. This helped me understand vocabulary creation, subword splitting, unknown tokens, tokenizer artifacts, and why tokenizer-model alignment is critical in fine-tuning workflows.

## 2 Crore Interview Question

If your custom tokenizer produces many `[UNK]` tokens and splits domain words badly, what will you do?

## Strong Answer

I would inspect tokenization outputs on representative domain samples. If I see many `[UNK]` tokens or excessive fragmentation, I would increase corpus size, add more domain-specific data, tune vocabulary size, consider byte-level BPE or SentencePiece, and evaluate sequence length distribution. If I am fine-tuning an existing pretrained model, I would usually prefer the original tokenizer unless the domain or language mismatch is severe, because changing tokenizer requires resizing embeddings and possibly continued pretraining.

## Memory Line

Corpus creates vocabulary.
BPE learns merges.
Tokenizer creates tokens.
Encoding creates input IDs and attention mask.
Decode helps debug.
`[UNK]` shows vocabulary weakness.
Vocab size controls fragmentation vs memory.
