"""
BERT Fine-Tuning on IMDb Sentiment Classification using Hugging Face Trainer API.

Recommended:
- Run training in Google Colab with GPU.
- Keep this script in GitHub as clean reproducible proof.

Flow:
Load IMDb dataset -> sample data -> tokenize -> prepare tensors -> load BERT -> train -> evaluate -> save -> predict.
"""

from pathlib import Path

from datasets import load_dataset
from transformers import (
    BertTokenizer,
    BertForSequenceClassification,
    Trainer,
    TrainingArguments,
    pipeline,
)


MODEL_NAME = "bert-base-uncased"
OUTPUT_DIR = Path("outputs/bert_finetuned_imdb")
LOG_DIR = Path("outputs/logs")
RESULT_FILE = Path("outputs/bert_imdb_trainer_api_output.txt")


def write_line(file, text: str = "") -> None:
    print(text)
    file.write(text + "\n")


def tokenize_function(example, tokenizer):
    return tokenizer(
        example["text"],
        padding="max_length",
        truncation=True,
        max_length=256,
    )


def prepare_dataset(tokenizer, file):
    write_line(file, "Loading IMDb dataset from Hugging Face Hub...")
    dataset = load_dataset("imdb")

    write_line(file, "Taking small samples for fast experimentation...")
    train_dataset = dataset["train"].shuffle(seed=42).select(range(1000))
    test_dataset = dataset["test"].shuffle(seed=42).select(range(500))

    write_line(file, "Tokenizing train and test datasets...")
    tokenized_train = train_dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)
    tokenized_test = test_dataset.map(lambda x: tokenize_function(x, tokenizer), batched=True)

    write_line(file, "Renaming label column to labels for Hugging Face Trainer...")
    tokenized_train = tokenized_train.rename_column("label", "labels")
    tokenized_test = tokenized_test.rename_column("label", "labels")

    write_line(file, "Setting dataset format to PyTorch tensors...")
    tokenized_train.set_format("torch", columns=["input_ids", "attention_mask", "labels"])
    tokenized_test.set_format("torch", columns=["input_ids", "attention_mask", "labels"])

    return tokenized_train, tokenized_test


def main():
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with RESULT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "BERT IMDb Fine-Tuning using Trainer API")
        write_line(file, "=" * 60)

        write_line(file, f"Loading tokenizer: {MODEL_NAME}")
        tokenizer = BertTokenizer.from_pretrained(MODEL_NAME)

        train_dataset, test_dataset = prepare_dataset(tokenizer, file)

        write_line(file, f"Loading model: {MODEL_NAME}")
        model = BertForSequenceClassification.from_pretrained(
            MODEL_NAME,
            num_labels=2,
        )

        write_line(file, "Creating TrainingArguments...")
        training_args = TrainingArguments(
            output_dir=str(OUTPUT_DIR),
            num_train_epochs=1,
            per_device_train_batch_size=8,
            per_device_eval_batch_size=8,
            learning_rate=2e-5,
            weight_decay=0.01,
            logging_dir=str(LOG_DIR),
            logging_steps=50,
            save_strategy="epoch",
            report_to="none",
        )

        write_line(file, "Creating Trainer...")
        trainer = Trainer(
            model=model,
            args=training_args,
            train_dataset=train_dataset,
            eval_dataset=test_dataset,
            tokenizer=tokenizer,
        )

        write_line(file, "Starting training...")
        write_line(file, "NOTE: Run this in Google Colab GPU for faster training.")
        trainer.train()

        write_line(file, "Evaluating model...")
        eval_results = trainer.evaluate()
        write_line(file, f"Evaluation results: {eval_results}")

        write_line(file, "Saving model and tokenizer...")
        trainer.save_model(str(OUTPUT_DIR))
        tokenizer.save_pretrained(str(OUTPUT_DIR))

        write_line(file, "Testing inference using pipeline...")
        classifier = pipeline(
            "text-classification",
            model=str(OUTPUT_DIR),
            tokenizer=str(OUTPUT_DIR),
        )

        sample_text = "This movie was amazing and I loved the acting."
        prediction = classifier(sample_text)

        write_line(file, f"Sample text: {sample_text}")
        write_line(file, f"Prediction: {prediction}")

        write_line(file, "Done.")


if __name__ == "__main__":
    main()
