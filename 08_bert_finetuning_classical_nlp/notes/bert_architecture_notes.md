# BERT Architecture Notes

## What is BERT?

BERT stands for **Bidirectional Encoder Representations from Transformers**.

It is a classical NLP model built using the **encoder side of the Transformer architecture**.

BERT is mainly used for language understanding tasks.

## BERT is Encoder-Only

Transformer architecture has two major parts:

- Encoder
- Decoder

BERT uses the **encoder** part.

GPT-style models use the **decoder** part.

## BERT-base vs BERT-large

| Model | Encoder Layers | Use Case |
|---|---:|---|
| BERT-base | 12 encoder layers | Faster, cheaper, common for practice and production |
| BERT-large | 24 encoder layers | More powerful but heavier |

## BERT vs GPT

| Feature | BERT | GPT |
|---|---|---|
| Architecture | Encoder-only | Decoder-only |
| Main strength | Understanding text | Generating text |
| Training style | MLM + NSP | Next-token prediction |
| Example tasks | Classification, NER, QA, embeddings | Chat, content generation, reasoning |
| Generative? | No | Yes |

## Simple Explanation

BERT is like a deep reader.

It reads the full sentence from both sides and understands the meaning.

GPT is like a writer.

It predicts the next word and keeps generating text.

## Technical Explanation

BERT takes tokenized text as input and passes it through multiple Transformer encoder layers.

Each encoder layer uses:

- Self-attention
- Feed-forward neural network
- Residual connections
- Layer normalization

The output is a contextual representation of each token.

For downstream tasks, we add a task-specific head on top of BERT.

## Why BERT Is Not a Generative Model

BERT does not generate long text token by token like GPT.

BERT is trained to understand the full context and produce representations.

Those representations are then used for:

- Classification
- Token classification
- Question answering
- Embedding generation

## Interview Memory Line

BERT understands. GPT generates.

BERT is encoder-only. GPT is decoder-only.

BERT is strong for NLP understanding tasks like classification, NER, QA, and embeddings.
