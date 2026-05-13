"""
02_hf_dataset_loading_preprocessing.py

Purpose:
Hands-on Hugging Face Datasets practice.

Video Topic:
Hugging Face Dataset Library, Preprocessing, and Visualization

This script demonstrates:
1. Loading a dataset from Hugging Face Hub
2. Inspecting dataset splits and features
3. Creating reproducible shuffled subsets
4. Filtering records
5. Adding a new feature using map()
6. Saving output proof for GitHub
"""

from pathlib import Path
from datasets import load_dataset


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "dataset_loading_preprocessing_output.txt"


def write_line(file, text: str = "") -> None:
    print(text)
    file.write(text + "\n")


def add_word_count(example: dict) -> dict:
    """
    Adds word_count column to each example.
    """
    text = example["text"]
    example["word_count"] = len(text.split())
    return example


def main() -> None:
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "=" * 80)
        write_line(file, "Hugging Face Dataset Loading and Preprocessing")
        write_line(file, "=" * 80)

        write_line(file, "\nLoading IMDb dataset from Hugging Face Hub...")
        dataset = load_dataset("imdb")

        write_line(file, "\nDataset object:")
        write_line(file, str(dataset))

        write_line(file, "\nAvailable splits:")
        write_line(file, str(dataset.keys()))

        train_data = dataset["train"]

        write_line(file, "\nTrain split details:")
        write_line(file, f"Number of rows: {train_data.num_rows}")
        write_line(file, f"Column names: {train_data.column_names}")
        write_line(file, f"Features: {train_data.features}")

        write_line(file, "\nFirst training example preview:")
        first_example = train_data[0]
        write_line(file, f"Label: {first_example['label']}")
        write_line(file, f"Text preview: {first_example['text'][:300]}...")

        write_line(file, "\nCreating reproducible shuffled dataset using seed=42...")
        shuffled_train = train_data.shuffle(seed=42)

        write_line(file, "\nSelecting a CPU-friendly subset of 100 samples...")
        small_subset = shuffled_train.select(range(100))
        write_line(file, f"Subset rows: {small_subset.num_rows}")

        write_line(file, "\nFiltering reviews with text length less than 500 characters...")
        short_reviews = small_subset.filter(lambda example: len(example["text"]) < 500)
        write_line(file, f"Short reviews found in subset: {short_reviews.num_rows}")

        write_line(file, "\nFiltering positive reviews with text length less than 700 characters...")
        positive_short_reviews = small_subset.filter(
            lambda example: example["label"] == 1 and len(example["text"]) < 700
        )
        write_line(file, f"Positive short reviews found: {positive_short_reviews.num_rows}")

        write_line(file, "\nAdding word_count column using map()...")
        subset_with_word_count = small_subset.map(add_word_count)

        write_line(file, "\nUpdated columns after map():")
        write_line(file, str(subset_with_word_count.column_names))

        write_line(file, "\nFirst 5 word counts:")
        for index in range(5):
            row = subset_with_word_count[index]
            write_line(
                file,
                f"Row {index}: label={row['label']}, word_count={row['word_count']}, text_preview={row['text'][:80]}..."
            )

        write_line(file, "\nDataset preprocessing completed successfully.")
        write_line(file, f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
