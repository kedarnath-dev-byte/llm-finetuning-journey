"""
08_hf_pipeline_api.py

Purpose:
Practice Hugging Face pipeline API for quick model inference.

Video Topic:
Hugging Face Prebuilt Pipeline API

This script demonstrates:
1. Sentiment analysis
2. Zero-shot classification
3. Text generation
4. Summarization with graceful error handling
5. Question answering with graceful error handling
6. Saving output proof for GitHub
"""

from pathlib import Path
from transformers import pipeline


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "hf_pipeline_api_output.txt"


def write_line(file, text: str = "") -> None:
    """
    Print output to terminal and save same output to file.
    """
    print(text)
    file.write(text + "\n")


def demo_sentiment_analysis(file) -> None:
    """
    Uses pipeline for sentiment analysis.
    """
    write_line(file, "\n" + "=" * 80)
    write_line(file, "1. Sentiment Analysis Pipeline")
    write_line(file, "=" * 80)

    classifier = pipeline(
        "sentiment-analysis",
        model="distilbert-base-uncased-finetuned-sst-2-english",
    )

    texts = [
        "I love learning Hugging Face because it makes AI development easier.",
        "This model is slow and the output is disappointing.",
    ]

    results = classifier(texts)

    for text, result in zip(texts, results):
        write_line(file, f"\nText: {text}")
        write_line(file, f"Result: {result}")

    write_line(file, "\nMeaning:")
    write_line(file, "The sentiment pipeline classifies text as POSITIVE or NEGATIVE.")


def demo_zero_shot_classification(file) -> None:
    """
    Uses pipeline for zero-shot classification.
    """
    write_line(file, "\n" + "=" * 80)
    write_line(file, "2. Zero-Shot Classification Pipeline")
    write_line(file, "=" * 80)

    classifier = pipeline(
        "zero-shot-classification",
        model="facebook/bart-large-mnli",
    )

    text = "This tutorial explains tokenization, embeddings, and transformer models."
    candidate_labels = ["education", "politics", "business", "agriculture"]

    result = classifier(text, candidate_labels)

    write_line(file, f"\nText: {text}")
    write_line(file, f"Candidate labels: {candidate_labels}")
    write_line(file, f"Result labels: {result['labels']}")
    write_line(file, f"Scores: {[round(score, 4) for score in result['scores']]}")

    write_line(file, "\nMeaning:")
    write_line(file, "Zero-shot classification predicts labels even without task-specific fine-tuning.")


def demo_text_generation(file) -> None:
    """
    Uses pipeline for text generation.
    """
    write_line(file, "\n" + "=" * 80)
    write_line(file, "3. Text Generation Pipeline")
    write_line(file, "=" * 80)

    generator = pipeline(
        "text-generation",
        model="gpt2",
    )

    prompt = "Hugging Face is useful for"
    result = generator(
        prompt,
        max_new_tokens=25,
        do_sample=False,
        pad_token_id=generator.tokenizer.eos_token_id,
    )

    write_line(file, f"\nPrompt: {prompt}")
    write_line(file, f"Generated text: {result[0]['generated_text']}")

    write_line(file, "\nMeaning:")
    write_line(file, "Text-generation pipeline uses next-token prediction to continue the prompt.")


def demo_summarization(file) -> None:
    """
    Uses pipeline for summarization if supported by installed Transformers version.
    """
    write_line(file, "\n" + "=" * 80)
    write_line(file, "4. Summarization Pipeline")
    write_line(file, "=" * 80)

    summarizer = pipeline(
        "summarization",
        model="sshleifer/distilbart-cnn-12-6",
    )

    text = (
        "Hugging Face provides a large ecosystem for machine learning developers. "
        "It includes pretrained models, datasets, tokenizers, evaluation tools, and deployment options. "
        "Developers use Hugging Face to prototype AI applications, fine-tune models, create embeddings, "
        "and share models or datasets through the Hub."
    )

    result = summarizer(text, max_length=45, min_length=15, do_sample=False)

    write_line(file, f"\nOriginal text: {text}")
    write_line(file, f"\nSummary: {result[0]['summary_text']}")


def demo_question_answering(file) -> None:
    """
    Uses pipeline for extractive question answering if supported by installed Transformers version.
    """
    write_line(file, "\n" + "=" * 80)
    write_line(file, "5. Question Answering Pipeline")
    write_line(file, "=" * 80)

    qa_pipeline = pipeline(
        "question-answering",
        model="distilbert-base-cased-distilled-squad",
    )

    context = (
        "Hugging Face is a platform for building, sharing, and using machine learning models. "
        "It provides models, datasets, Spaces, tokenizers, and libraries for AI development."
    )

    question = "What does Hugging Face provide?"

    result = qa_pipeline(question=question, context=context)

    write_line(file, f"\nContext: {context}")
    write_line(file, f"Question: {question}")
    write_line(file, f"Answer: {result['answer']}")
    write_line(file, f"Score: {result['score']:.4f}")


def main() -> None:
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "=" * 80)
        write_line(file, "Hugging Face Pipeline API")
        write_line(file, "=" * 80)

        demo_sentiment_analysis(file)
        demo_zero_shot_classification(file)
        demo_text_generation(file)

        try:
            demo_summarization(file)
        except Exception as error:
            write_line(file, "\nSummarization pipeline skipped due to environment/version issue:")
            write_line(file, str(error))

        try:
            demo_question_answering(file)
        except Exception as error:
            write_line(file, "\nQuestion-answering pipeline skipped due to environment/version issue:")
            write_line(file, str(error))

        write_line(file, "\n" + "=" * 80)
        write_line(file, "Summary")
        write_line(file, "=" * 80)

        write_line(file, "\nPipeline API is useful for rapid prototyping.")
        write_line(file, "It hides tokenizer/model boilerplate and gives quick inference outputs.")
        write_line(file, "For production or fine-tuning, we may move from pipeline to AutoModel, Trainer, or custom inference code.")
        write_line(file, "If a pipeline task is unsupported in the installed Transformers version, handle it gracefully and document the issue.")

        write_line(file, "\nPipeline API practical completed successfully.")
        write_line(file, f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
