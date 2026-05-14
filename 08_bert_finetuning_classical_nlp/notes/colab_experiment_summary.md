# Colab BERT IMDb Fine-Tuning Experiment Summary

## Platform

Google Colab with Tesla T4 GPU.

## Model

`bert-base-uncased`

## Task

IMDb binary sentiment classification.

- LABEL_0 = Negative
- LABEL_1 = Positive

## Dataset Sample

- Training rows: 1000
- Test rows: 500

## Training Setup

- Epochs: 1
- Batch size: 8
- Learning rate: 2e-5
- Weight decay: 0.01
- Max sequence length: 256

## Training Result

- Global steps: 125
- Training runtime: around 62.84 seconds
- Training loss: around 0.5109

## Evaluation Result

- Evaluation loss: around 0.3375
- Evaluation runtime: around 10.15 seconds

## Inference Proof

The fine-tuned model correctly predicted:

1. Positive review:
   - Text: This movie was amazing and I loved the acting.
   - Prediction: LABEL_1
   - Score: around 0.77

2. Negative review:
   - Text: The film was boring, slow, and badly written.
   - Prediction: LABEL_0
   - Score: around 0.86

3. Mixed but positive review:
   - Text: The story was okay, but the acting was excellent.
   - Prediction: LABEL_1
   - Score: around 0.62

## Learning

This experiment proves the complete BERT fine-tuning lifecycle:

Raw IMDb text
-> BERT tokenizer
-> input_ids and attention_mask
-> BertForSequenceClassification
-> Trainer API
-> GPU fine-tuning
-> evaluation
-> save model and tokenizer
-> reload with pipeline
-> inference on new reviews

## Interview Memory Line

BERT is not generative. BERT understands text using encoder representations, and the classification head converts that understanding into positive or negative sentiment.
