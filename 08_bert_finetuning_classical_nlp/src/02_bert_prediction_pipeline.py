"""
Prediction script for a fine-tuned BERT IMDb sentiment classifier.

Use this after the fine-tuned model and tokenizer are saved in:
outputs/bert_finetuned_imdb/

Recommended:
- Train in Google Colab GPU.
- Copy saved model output or document inference screenshots in GitHub.
"""

from pathlib import Path

from transformers import pipeline


MODEL_DIR = Path("outputs/bert_finetuned_imdb")
RESULT_FILE = Path("outputs/bert_prediction_pipeline_output.txt")


def write_line(file, text: str = "") -> None:
    print(text)
    file.write(text + "\n")


def main():
    RESULT_FILE.parent.mkdir(parents=True, exist_ok=True)

    with RESULT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "BERT Fine-Tuned Model Prediction Pipeline")
        write_line(file, "=" * 60)

        if not MODEL_DIR.exists():
            write_line(file, f"Model directory not found: {MODEL_DIR}")
            write_line(file, "Train the model first using 01_bert_imdb_trainer_api.py in Colab GPU.")
            return

        write_line(file, f"Loading fine-tuned model from: {MODEL_DIR}")

        classifier = pipeline(
            "text-classification",
            model=str(MODEL_DIR),
            tokenizer=str(MODEL_DIR),
        )

        sample_texts = [
            "This movie was amazing and I loved the acting.",
            "The film was boring, slow, and badly written.",
            "The story was okay, but the acting was excellent.",
        ]

        for text in sample_texts:
            prediction = classifier(text)
            write_line(file, f"Text: {text}")
            write_line(file, f"Prediction: {prediction}")
            write_line(file)

        write_line(file, "Done.")


if __name__ == "__main__":
    main()
