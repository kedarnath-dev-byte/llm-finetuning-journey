"""
03_dataset_visualization_analysis.py

Purpose:
Perform CPU-friendly dataset visualization and text analysis using Hugging Face Datasets.

Video Topic:
Hugging Face Dataset Library, Preprocessing, and Visualization

This script demonstrates:
1. Loading IMDb dataset
2. Taking a reproducible subset
3. Analyzing label distribution
4. Analyzing word count distribution
5. Finding most common words
6. Saving charts and summary outputs for GitHub proof
"""

from pathlib import Path
from collections import Counter
import re

import pandas as pd
import matplotlib.pyplot as plt
from datasets import load_dataset


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

SUMMARY_FILE = OUTPUT_DIR / "dataset_visualization_analysis_output.txt"
LABEL_CHART = OUTPUT_DIR / "imdb_label_distribution.png"
WORD_COUNT_CHART = OUTPUT_DIR / "imdb_word_count_distribution.png"
COMMON_WORDS_CHART = OUTPUT_DIR / "imdb_top_common_words.png"


def clean_and_split_words(text: str) -> list[str]:
    """
    Converts text into lowercase words and removes simple punctuation.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z\s]", " ", text)
    words = text.split()

    stopwords = {
        "the", "a", "an", "and", "or", "is", "was", "were", "to", "of", "in",
        "it", "this", "that", "i", "for", "with", "as", "on", "but", "movie",
        "film", "br", "be", "are", "at", "by", "from", "have", "has", "had"
    }

    return [word for word in words if word not in stopwords and len(word) > 2]


def main() -> None:
    print("=" * 80)
    print("IMDb Dataset Visualization and Analysis")
    print("=" * 80)

    print("\nLoading IMDb dataset...")
    dataset = load_dataset("imdb")

    print("\nCreating reproducible subset of 1000 training examples...")
    train_subset = dataset["train"].shuffle(seed=42).select(range(1000))

    print("\nConverting subset to pandas DataFrame for analysis...")
    df = pd.DataFrame(train_subset)

    df["label_name"] = df["label"].map({0: "negative", 1: "positive"})
    df["word_count"] = df["text"].apply(lambda text: len(text.split()))

    label_counts = df["label_name"].value_counts()
    average_word_count = df["word_count"].mean()
    max_word_count = df["word_count"].max()
    min_word_count = df["word_count"].min()

    print("\nSaving label distribution chart...")
    plt.figure(figsize=(6, 4))
    label_counts.plot(kind="bar")
    plt.title("IMDb Label Distribution in 1000-Sample Subset")
    plt.xlabel("Sentiment Label")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    plt.savefig(LABEL_CHART)
    plt.close()

    print("Saving word count distribution chart...")
    plt.figure(figsize=(8, 4))
    df["word_count"].plot(kind="hist", bins=30)
    plt.title("IMDb Review Word Count Distribution")
    plt.xlabel("Word Count")
    plt.ylabel("Number of Reviews")
    plt.tight_layout()
    plt.savefig(WORD_COUNT_CHART)
    plt.close()

    print("Finding top common words...")
    all_words = []
    for text in df["text"]:
        all_words.extend(clean_and_split_words(text))

    top_words = Counter(all_words).most_common(20)
    top_words_df = pd.DataFrame(top_words, columns=["word", "count"])

    print("Saving top common words chart...")
    plt.figure(figsize=(10, 5))
    plt.bar(top_words_df["word"], top_words_df["count"])
    plt.title("Top 20 Common Words in IMDb Subset")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.savefig(COMMON_WORDS_CHART)
    plt.close()

    print("\nSaving summary output...")
    with SUMMARY_FILE.open("w", encoding="utf-8") as file:
        file.write("IMDb Dataset Visualization and Analysis\n")
        file.write("=" * 80 + "\n\n")

        file.write("Dataset used: imdb\n")
        file.write("Split used: train\n")
        file.write("Subset size: 1000 examples\n")
        file.write("Shuffle seed: 42\n\n")

        file.write("Label distribution:\n")
        for label, count in label_counts.items():
            file.write(f"- {label}: {count}\n")

        file.write("\nWord count statistics:\n")
        file.write(f"- Average word count: {average_word_count:.2f}\n")
        file.write(f"- Minimum word count: {min_word_count}\n")
        file.write(f"- Maximum word count: {max_word_count}\n")

        file.write("\nTop 20 common words:\n")
        for word, count in top_words:
            file.write(f"- {word}: {count}\n")

        file.write("\nGenerated chart files:\n")
        file.write(f"- {LABEL_CHART}\n")
        file.write(f"- {WORD_COUNT_CHART}\n")
        file.write(f"- {COMMON_WORDS_CHART}\n")

        file.write("\nInterview explanation:\n")
        file.write(
            "I performed exploratory data analysis on the IMDb dataset before tokenization and fine-tuning. "
            "I checked label distribution, review length distribution, and frequent words to understand dataset balance, "
            "sequence length behavior, and basic text patterns. This is important because data quality directly impacts "
            "fine-tuning performance.\n"
        )

    print("\nVisualization analysis completed successfully.")
    print(f"Summary saved to: {SUMMARY_FILE}")
    print(f"Charts saved to: {OUTPUT_DIR}")


if __name__ == "__main__":
    main()
