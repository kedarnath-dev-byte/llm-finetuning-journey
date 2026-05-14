# Task-Specific Heads in BERT

## Core Idea

BERT produces contextual vector representations.

But raw BERT vectors alone do not directly give final task answers.

To solve a specific task, we add a task-specific head on top of BERT.

## What is a Head?

A head is a small neural network layer added on top of the base BERT model.

Usually, it contains:

- Dense/feed-forward layer
- Dropout
- Output layer
- Softmax or task-specific output logic

## Why Do We Need Heads?

The same BERT base model can understand text.

But different tasks need different output formats.

Examples:

| Task | Output Needed | Head Type |
|---|---|---|
| Sentiment classification | Positive/Negative label | Sequence classification head |
| Topic classification | Topic label | Sequence classification head |
| NER | Label for each token | Token classification head |
| POS tagging | Part-of-speech label for each token | Token classification head |
| Question answering | Start and end span | QA head |
| Embedding generation | Vector representation | No classification head needed |

## BERTForSequenceClassification

Used for sentence-level or document-level classification.

Examples:

- IMDb sentiment classification
- Customer review classification
- Support ticket category prediction
- Email spam classification
- Student doubt category classification

## BERTForTokenClassification

Used when every token needs a label.

Examples:

- Named Entity Recognition
- POS tagging
- Medical entity extraction
- Legal clause tagging
- Resume skill extraction

## BERTForQuestionAnswering

Used for extractive question answering.

The model predicts:

- Start token position
- End token position

The answer is extracted from the given context.

## Simple Analogy

BERT is like a powerful brain.

The head is like the job role assigned to that brain.

Same brain:

- With classification head: decides positive or negative
- With NER head: identifies names, places, organizations
- With QA head: finds answer span from a paragraph

## Technical Explanation

BERT encoder outputs hidden states.

For classification, we usually use the CLS token representation and pass it through a classification head.

For token classification, we use each token representation and classify each token.

For QA, we predict start and end positions over the token sequence.

## Important Interview Point

The base BERT architecture can remain similar, but the head changes based on the downstream task.

## 2 Crore Interview Answer

In production, I would choose the BERT head based on the business output required.

If the business wants one label per document, I use sequence classification.

If the business wants entities inside text, I use token classification.

If the business wants answer extraction from a passage, I use question answering.

This allows the same pretrained BERT foundation to be adapted to multiple enterprise NLP tasks.
