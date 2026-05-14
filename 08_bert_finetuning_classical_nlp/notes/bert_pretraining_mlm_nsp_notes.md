# BERT Pretraining: MLM and NSP Notes

## Two Training Stages of BERT

BERT training can be understood in two major stages:

1. Self-supervised pretraining
2. Supervised fine-tuning

## Stage 1: Self-Supervised Pretraining

In the first stage, BERT is trained on a huge amount of raw text data.

This data does not require manual labels.

That is why it is often called:

- Unsupervised pretraining
- Self-supervised pretraining

Self-supervised is more technically accurate because labels are created from the text itself.

## BERT Pretraining Tasks

BERT was pretrained mainly using:

1. Masked Language Modeling
2. Next Sentence Prediction

## 1. Masked Language Modeling

Masked Language Modeling is also called MLM.

In MLM, some words in a sentence are hidden using a mask token.

BERT tries to predict the missing word using the left and right context.

### Example

Original sentence:

The capital of France is Paris.

Masked sentence:

The capital of France is [MASK].

BERT should predict:

Paris

## Why MLM Matters

MLM teaches BERT deep bidirectional understanding.

It can look at both left context and right context.

That is why BERT is strong for understanding tasks.

## 2. Next Sentence Prediction

Next Sentence Prediction is also called NSP.

In NSP, BERT learns whether two sentences logically follow each other.

### Example

Sentence A:

The student studied hard for the exam.

Sentence B:

He scored good marks.

These two sentences are related.

But:

Sentence A:

The student studied hard for the exam.

Sentence B:

The mango tree is near the river.

These two sentences are not strongly related.

## Why NSP Matters

NSP helps BERT understand sentence relationships.

This is useful for tasks like:

- Question answering
- Natural language inference
- Document understanding
- Sentence pair classification

## Stage 2: Supervised Fine-Tuning

After pretraining, BERT is fine-tuned on labeled task-specific data.

Examples:

- Sentiment classification
- Named entity recognition
- Question answering
- Intent classification
- Support ticket classification

## Simple Analogy

Pretraining is like a student reading thousands of books alone and learning language patterns.

Fine-tuning is like a teacher giving the student exam-specific questions with correct answers.

## Technical Summary

BERT pretraining creates general language understanding.

Fine-tuning adapts that understanding to a specific task using labeled data.

## BERT vs GPT Training

| Model | Pretraining Style | Main Skill |
|---|---|---|
| BERT | MLM + NSP | Understand text |
| GPT | Causal next-token prediction | Generate text |

## Interview Memory Line

BERT learns by filling blanks and understanding sentence relationships.

GPT learns by predicting the next word.
