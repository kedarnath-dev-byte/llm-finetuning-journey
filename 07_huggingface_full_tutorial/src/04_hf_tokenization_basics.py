"""
04_hf_tokenization_basics.py

Purpose:
Understand Hugging Face tokenization basics.

Video Topic:
Tokenization in Hugging Face

This script demonstrates:
1. Loading a pretrained tokenizer
2. Converting text into tokens
3. Converting text into input IDs
4. Understanding attention masks
5. Understanding token type IDs
6. Applying padding and truncation
7. Tokenizing multiple sentences as a batch
8. Saving output proof for GitHub
"""

from pathlib import Path
from transformers import AutoTokenizer


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "tokenization_basics_output.txt"


def write_line(file, text: str = "") -> None:
    """
    Print output to terminal and save the same output to a file.
    """
    print(text)
    file.write(text + "\n")


def main() -> None:
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "=" * 80)
        write_line(file, "Hugging Face Tokenization Basics")
        write_line(file, "=" * 80)

        model_name = "bert-base-uncased"

        write_line(file, f"\nLoading tokenizer for model: {model_name}")
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        sentence = "Hello, Hugging Face! I am learning LLM fine-tuning."

        write_line(file, "\nOriginal sentence:")
        write_line(file, sentence)

        tokens = tokenizer.tokenize(sentence)
        write_line(file, "\nStep 1: Tokens")
        write_line(file, str(tokens))

        token_ids = tokenizer.convert_tokens_to_ids(tokens)
        write_line(file, "\nStep 2: Token IDs")
        write_line(file, str(token_ids))

        encoded = tokenizer(sentence, return_tensors="pt")

        write_line(file, "\nStep 3: Full encoded output")
        write_line(file, str(encoded))

        write_line(file, "\nInput IDs:")
        write_line(file, str(encoded["input_ids"]))

        write_line(file, "\nToken Type IDs:")
        if "token_type_ids" in encoded:
            write_line(file, str(encoded["token_type_ids"]))
        else:
            write_line(file, "This tokenizer/model does not return token_type_ids.")

        write_line(file, "\nAttention Mask:")
        write_line(file, str(encoded["attention_mask"]))

        write_line(file, "\nDecoded text from input IDs:")
        decoded_text = tokenizer.decode(encoded["input_ids"][0])
        write_line(file, decoded_text)

        write_line(file, "\n" + "-" * 80)
        write_line(file, "Padding and Truncation Example")
        write_line(file, "-" * 80)

        long_sentence = (
            "Hugging Face tokenization is important because transformer models do not understand raw text directly. "
            "They understand numerical token IDs created by a tokenizer."
        )

        padded_truncated = tokenizer(
            long_sentence,
            padding="max_length",
            truncation=True,
            max_length=20,
            return_tensors="pt",
        )

        write_line(file, "\nLong sentence:")
        write_line(file, long_sentence)

        write_line(file, "\nEncoded with padding='max_length', truncation=True, max_length=20:")
        write_line(file, str(padded_truncated))

        write_line(file, "\nDecoded padded/truncated input:")
        write_line(file, tokenizer.decode(padded_truncated["input_ids"][0]))

        write_line(file, "\n" + "-" * 80)
        write_line(file, "Batch Tokenization Example")
        write_line(file, "-" * 80)

        batch_sentences = [
            "I love learning Hugging Face.",
            "Tokenization converts text into model-readable numbers.",
            "Fine-tuning adapts a pretrained model to a specific task.",
        ]

        batch_encoded = tokenizer(
            batch_sentences,
            padding=True,
            truncation=True,
            return_tensors="pt",
        )

        write_line(file, "\nBatch sentences:")
        for sentence_index, text in enumerate(batch_sentences):
            write_line(file, f"{sentence_index + 1}. {text}")

        write_line(file, "\nBatch input_ids shape:")
        write_line(file, str(batch_encoded["input_ids"].shape))

        write_line(file, "\nBatch attention_mask shape:")
        write_line(file, str(batch_encoded["attention_mask"].shape))

        write_line(file, "\nFirst batch input IDs:")
        write_line(file, str(batch_encoded["input_ids"][0]))

        write_line(file, "\nFirst batch decoded text:")
        write_line(file, tokenizer.decode(batch_encoded["input_ids"][0]))

        write_line(file, "\nTokenization basics completed successfully.")
        write_line(file, f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
