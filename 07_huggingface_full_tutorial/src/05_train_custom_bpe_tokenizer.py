"""
05_train_custom_bpe_tokenizer.py

Purpose:
Train a small custom BPE tokenizer using Hugging Face Tokenizers.

Video Topic:
Train your own tokenizer and use it

This script demonstrates:
1. Creating a small domain corpus
2. Training a BPE tokenizer
3. Using whitespace pre-tokenization
4. Saving tokenizer JSON
5. Loading tokenizer back as a fast tokenizer
6. Encoding sample sentences
7. Saving output proof for GitHub
"""

from pathlib import Path

from tokenizers import Tokenizer
from tokenizers.models import BPE
from tokenizers.pre_tokenizers import Whitespace
from tokenizers.trainers import BpeTrainer
from transformers import PreTrainedTokenizerFast


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

TOKENIZER_DIR = Path("outputs/custom_bpe_tokenizer")
TOKENIZER_DIR.mkdir(exist_ok=True)

RAW_TOKENIZER_FILE = TOKENIZER_DIR / "custom_tokenizer.json"
FAST_TOKENIZER_DIR = TOKENIZER_DIR / "hf_fast_tokenizer"

OUTPUT_FILE = OUTPUT_DIR / "custom_bpe_tokenizer_output.txt"


def write_line(file, text: str = "") -> None:
    """
    Print output to terminal and write the same output to a file.
    """
    print(text)
    file.write(text + "\n")


def build_training_corpus() -> list[str]:
    """
    Creates a small domain-style corpus for tokenizer training.

    In real projects, this corpus can come from:
    - education notes
    - agriculture FAQs
    - hospital FAQs
    - finance documents
    - legal contracts
    - company support tickets
    """
    return [
        "Hugging Face helps developers build and share machine learning models.",
        "Fine tuning adapts a pretrained model to a specific downstream task.",
        "Tokenization converts human language into model readable numbers.",
        "Attention masks help transformer models ignore padding tokens.",
        "BPE tokenization breaks rare words into useful subword units.",
        "Education AI tutors can explain concepts using student friendly language.",
        "Agriculture AI assistants can answer crop disease and soil related questions.",
        "Healthcare AI systems must be safe and require human expert supervision.",
        "Finance AI assistants can summarize reports and classify customer requests.",
        "Legal AI tools can help summarize contracts and retrieve relevant clauses.",
        "A production LLM system needs data quality, evaluation, safety, and monitoring.",
    ]


def train_bpe_tokenizer(corpus: list[str]) -> Tokenizer:
    """
    Trains a Byte Pair Encoding tokenizer on the provided corpus.
    """
    tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
    tokenizer.pre_tokenizer = Whitespace()

    trainer = BpeTrainer(
        vocab_size=120,
        special_tokens=["[UNK]", "[PAD]", "[CLS]", "[SEP]", "[MASK]"],
    )

    tokenizer.train_from_iterator(corpus, trainer=trainer)
    return tokenizer


def load_as_fast_tokenizer(raw_tokenizer_file: Path) -> PreTrainedTokenizerFast:
    """
    Loads the saved tokenizer JSON as a Hugging Face fast tokenizer.
    """
    return PreTrainedTokenizerFast(
        tokenizer_file=str(raw_tokenizer_file),
        unk_token="[UNK]",
        pad_token="[PAD]",
        cls_token="[CLS]",
        sep_token="[SEP]",
        mask_token="[MASK]",
    )


def main() -> None:
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "=" * 80)
        write_line(file, "Custom BPE Tokenizer Training")
        write_line(file, "=" * 80)

        corpus = build_training_corpus()

        write_line(file, "\nTraining corpus size:")
        write_line(file, str(len(corpus)))

        write_line(file, "\nSample corpus lines:")
        for index, line in enumerate(corpus[:3], start=1):
            write_line(file, f"{index}. {line}")

        write_line(file, "\nTraining BPE tokenizer...")
        tokenizer = train_bpe_tokenizer(corpus)

        write_line(file, "\nSaving raw tokenizer JSON...")
        tokenizer.save(str(RAW_TOKENIZER_FILE))
        write_line(file, f"Saved raw tokenizer file: {RAW_TOKENIZER_FILE}")

        write_line(file, "\nLoading tokenizer back as PreTrainedTokenizerFast...")
        fast_tokenizer = load_as_fast_tokenizer(RAW_TOKENIZER_FILE)

        write_line(file, "\nSaving Hugging Face fast tokenizer folder...")
        fast_tokenizer.save_pretrained(str(FAST_TOKENIZER_DIR))
        write_line(file, f"Saved fast tokenizer folder: {FAST_TOKENIZER_DIR}")

        test_sentences = [
            "Fine tuning helps adapt models for education AI.",
            "Agriculture assistants can answer crop questions.",
            "UnknownNewDomainWord should be handled by subword tokenization.",
        ]

        write_line(file, "\nTesting custom tokenizer:")
        for sentence in test_sentences:
            write_line(file, "\nOriginal sentence:")
            write_line(file, sentence)

            encoding = fast_tokenizer(sentence)

            write_line(file, "Tokens:")
            write_line(file, str(fast_tokenizer.tokenize(sentence)))

            write_line(file, "Input IDs:")
            write_line(file, str(encoding["input_ids"]))

            write_line(file, "Attention Mask:")
            write_line(file, str(encoding["attention_mask"]))

            write_line(file, "Decoded text:")
            write_line(file, fast_tokenizer.decode(encoding["input_ids"]))

        write_line(file, "\nTokenizer vocabulary size:")
        write_line(file, str(fast_tokenizer.vocab_size))

        write_line(file, "\nCustom BPE tokenizer training completed successfully.")
        write_line(file, f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
