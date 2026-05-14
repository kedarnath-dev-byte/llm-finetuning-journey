# Colab vs Laptop Decision for BERT Fine-Tuning

## Final Decision

For this module, training will be done in Google Colab.

Laptop will be used for GitHub structure, scripts, notes, outputs, screenshots, and commits.

## Why Colab for Training?

BERT fine-tuning is compute-heavy compared to simple Hugging Face pipeline usage.

It benefits from GPU acceleration.

In the previous Hugging Face module, local PyTorch showed:

- CUDA available: False
- CPU-only environment

So laptop is not ideal for training BERT.

## What to Do in Colab

Use Google Colab for:

- Installing training libraries
- Selecting GPU runtime
- Loading IMDb dataset
- Loading BERT tokenizer
- Tokenizing data
- Loading BertForSequenceClassification
- Running Trainer API
- Training the model
- Evaluating the model
- Saving model and tokenizer
- Testing prediction pipeline
- Taking screenshots of training/evaluation output

## What to Do on Laptop

Use laptop for:

- Creating project folders
- Saving notebook in GitHub repo
- Creating clean Python scripts
- Writing notes
- Writing README
- Saving output text files
- Saving screenshots from Colab
- Git add, commit, and push

## Workflow

Colab GPU:
Train and test BERT model.

Laptop:
Document, clean, organize, and push proof to GitHub.

## Interview Explanation

I did not blindly train everything locally.

I checked hardware limitations and selected Colab GPU for model fine-tuning.

This shows practical engineering judgment because platform choice affects cost, speed, reproducibility, and training feasibility.

## Memory Line

Colab trains the model.

Laptop builds the portfolio proof.
