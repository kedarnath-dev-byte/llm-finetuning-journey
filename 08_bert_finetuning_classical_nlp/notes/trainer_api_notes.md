# Hugging Face Trainer API Notes

## What is Trainer API?

The Hugging Face Trainer API is a high-level training interface.

It helps us fine-tune Transformer models without manually writing the full PyTorch training loop.

## Why Trainer API Is Useful

Trainer handles many things automatically:

- Forward pass
- Loss calculation
- Backward pass
- Optimizer step
- Evaluation
- Checkpoint saving
- Logging
- Batch handling
- Device handling

## BERT Fine-Tuning Flow in This Video

The video follows this practical flow:

Load IMDb dataset
-> Take small train/test sample
-> Load BERT tokenizer
-> Tokenize text
-> Apply padding and truncation
-> Rename label column to labels
-> Convert data to PyTorch tensor format
-> Load BertForSequenceClassification
-> Define TrainingArguments
-> Create Trainer
-> trainer.train()
-> trainer.evaluate()
-> Save model and tokenizer
-> Load model for prediction
-> Use pipeline for inference

## Key Components

### Dataset

The IMDb dataset is used for sentiment classification.

The trainer takes:

- 1000 training samples
- 500 testing samples

This keeps the experiment fast in free Colab GPU.

### Tokenizer

Tokenizer converts raw text into model-readable format:

- input_ids
- attention_mask
- labels

### Padding

Padding makes all sequences the same length.

If max_length is 256 and a sentence has only 100 tokens, the remaining 156 positions are padded.

### Truncation

Truncation cuts long sequences.

If max_length is 256 and a sentence has 300 tokens, only 256 tokens are kept.

### Model

The model used is BertForSequenceClassification.

This means BERT plus a classification head.

For IMDb sentiment classification, number of labels is 2:

- negative
- positive

### TrainingArguments

TrainingArguments stores training configuration.

Important values:

- output_dir
- num_train_epochs
- per_device_train_batch_size
- per_device_eval_batch_size
- learning_rate
- weight_decay
- logging_dir
- report_to

### Trainer

Trainer connects:

- model
- training arguments
- train dataset
- eval dataset
- tokenizer

Then training starts with trainer.train().

## Why Small Learning Rate?

BERT is already pretrained.

We do not want to destroy its learned knowledge.

So we use a small learning rate during fine-tuning.

## Full Fine-Tuning vs Layer Freezing

In BERT fine-tuning, we can choose:

1. Full fine-tuning
2. Fine-tune selected layers
3. Fine-tune only the final classification head

## When to Use Full Fine-Tuning

Use full fine-tuning when:

- You have enough labeled data
- Your domain is different from general text
- You have GPU resources
- You want better task-specific accuracy

## When to Freeze Layers

Freeze layers when:

- Dataset is small
- GPU is limited
- You want faster training
- You want to reduce overfitting

## Evaluation

After training, we call trainer.evaluate().

This returns metrics like:

- evaluation loss
- runtime
- samples per second
- steps per second

## Saving Model and Tokenizer

Both model and tokenizer should be saved.

Why?

The model contains learned weights.

The tokenizer contains the vocabulary and tokenization rules.

If we save only the model and not the tokenizer, inference may break or become inconsistent.

## Interview Memory Line

Trainer API is a shortcut for standard Transformer fine-tuning.

It connects model, data, tokenizer, training configuration, evaluation, checkpoints, and logging into one clean workflow.
