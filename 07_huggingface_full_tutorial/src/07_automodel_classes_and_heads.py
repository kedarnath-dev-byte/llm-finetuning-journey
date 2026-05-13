"""
07_automodel_classes_and_heads.py

Purpose:
Understand Hugging Face AutoModel classes and task-specific heads.

Video Topic:
AutoModel classes, task-specific heads, and AutoConfig

This script demonstrates:
1. AutoModel for base transformer hidden states
2. AutoModelForSequenceClassification for sentiment classification
3. AutoModelForCausalLM for text generation
4. AutoConfig for inspecting model configuration
5. Saving output proof for GitHub
"""

from pathlib import Path

import torch
from transformers import (
    AutoTokenizer,
    AutoModel,
    AutoModelForSequenceClassification,
    AutoModelForCausalLM,
    AutoConfig,
)


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "automodel_classes_and_heads_output.txt"


def write_line(file, text: str = "") -> None:
    """
    Print output to terminal and save same output to file.
    """
    print(text)
    file.write(text + "\n")


def demo_base_automodel(file) -> None:
    """
    Demonstrates AutoModel.

    AutoModel loads the base transformer model without a task-specific head.
    It returns hidden states/embeddings.
    """
    model_name = "bert-base-uncased"
    text = "Hugging Face AutoModel gives hidden states."

    write_line(file, "\n" + "=" * 80)
    write_line(file, "1. AutoModel: Base Transformer Model")
    write_line(file, "=" * 80)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModel.from_pretrained(model_name)
    model.eval()

    encoded_input = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**encoded_input)

    write_line(file, f"Model used: {model_name}")
    write_line(file, f"Input text: {text}")
    write_line(file, f"Output type: {type(output)}")
    write_line(file, f"last_hidden_state shape: {tuple(output.last_hidden_state.shape)}")

    write_line(file, "\nMeaning:")
    write_line(
        file,
        "AutoModel gives token-level hidden states. It does not directly classify or generate text."
    )


def demo_sequence_classification(file) -> None:
    """
    Demonstrates AutoModelForSequenceClassification.

    This model has a classification head on top of the base transformer.
    """
    model_name = "distilbert-base-uncased-finetuned-sst-2-english"
    text = "I really enjoyed learning Hugging Face today."

    write_line(file, "\n" + "=" * 80)
    write_line(file, "2. AutoModelForSequenceClassification: Classification Head")
    write_line(file, "=" * 80)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForSequenceClassification.from_pretrained(model_name)
    model.eval()

    encoded_input = tokenizer(text, return_tensors="pt")

    with torch.no_grad():
        output = model(**encoded_input)

    logits = output.logits
    probabilities = torch.softmax(logits, dim=1)
    predicted_class_id = int(torch.argmax(probabilities, dim=1).item())
    predicted_label = model.config.id2label[predicted_class_id]

    write_line(file, f"Model used: {model_name}")
    write_line(file, f"Input text: {text}")
    write_line(file, f"Logits: {logits.tolist()}")
    write_line(file, f"Probabilities: {probabilities.tolist()}")
    write_line(file, f"Predicted class id: {predicted_class_id}")
    write_line(file, f"Predicted label: {predicted_label}")

    write_line(file, "\nMeaning:")
    write_line(
        file,
        "AutoModelForSequenceClassification adds a classification head on top of the transformer."
    )


def demo_causal_lm(file) -> None:
    """
    Demonstrates AutoModelForCausalLM.

    Causal LM models predict the next token and can generate text.
    """
    model_name = "gpt2"
    prompt = "Hugging Face is useful for"

    write_line(file, "\n" + "=" * 80)
    write_line(file, "3. AutoModelForCausalLM: Text Generation Head")
    write_line(file, "=" * 80)

    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    model.eval()

    encoded_input = tokenizer(prompt, return_tensors="pt")

    with torch.no_grad():
        generated_ids = model.generate(
            **encoded_input,
            max_new_tokens=20,
            do_sample=False,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)

    write_line(file, f"Model used: {model_name}")
    write_line(file, f"Prompt: {prompt}")
    write_line(file, f"Generated text: {generated_text}")

    write_line(file, "\nMeaning:")
    write_line(
        file,
        "AutoModelForCausalLM is used for decoder-style next-token prediction and text generation."
    )


def demo_autoconfig(file) -> None:
    """
    Demonstrates AutoConfig.

    AutoConfig loads model configuration without loading full model weights.
    """
    model_name = "bert-base-uncased"

    write_line(file, "\n" + "=" * 80)
    write_line(file, "4. AutoConfig: Model Architecture Configuration")
    write_line(file, "=" * 80)

    config = AutoConfig.from_pretrained(model_name)

    write_line(file, f"Model used: {model_name}")
    write_line(file, f"Model type: {config.model_type}")
    write_line(file, f"Hidden size: {config.hidden_size}")
    write_line(file, f"Number of hidden layers: {config.num_hidden_layers}")
    write_line(file, f"Number of attention heads: {config.num_attention_heads}")
    write_line(file, f"Vocabulary size: {config.vocab_size}")

    write_line(file, "\nChanging num_labels in config for a custom classification task...")
    config.num_labels = 5
    write_line(file, f"Updated num_labels: {config.num_labels}")

    write_line(file, "\nMeaning:")
    write_line(
        file,
        "AutoConfig helps inspect and modify model architecture settings before loading or fine-tuning."
    )


def main() -> None:
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "=" * 80)
        write_line(file, "Hugging Face AutoModel Classes and Task-Specific Heads")
        write_line(file, "=" * 80)

        demo_base_automodel(file)
        demo_sequence_classification(file)
        demo_causal_lm(file)
        demo_autoconfig(file)

        write_line(file, "\n" + "=" * 80)
        write_line(file, "Summary")
        write_line(file, "=" * 80)

        write_line(file, "\nAutoModel:")
        write_line(file, "Base transformer model. Useful for embeddings and hidden states.")

        write_line(file, "\nAutoModelForSequenceClassification:")
        write_line(file, "Base model plus classification head. Useful for sentiment, topic, spam, intent classification.")

        write_line(file, "\nAutoModelForCausalLM:")
        write_line(file, "Decoder-style language model head. Useful for text generation and next-token prediction.")

        write_line(file, "\nAutoConfig:")
        write_line(file, "Loads architecture metadata such as hidden size, layers, attention heads, vocab size, and labels.")

        write_line(file, "\nProduction learning:")
        write_line(
            file,
            "Choosing the correct AutoModel class is important because each class attaches a different task-specific head."
        )
        write_line(
            file,
            "Wrong class selection can produce wrong outputs, shape errors, or an unsuitable model for the task."
        )

        write_line(file, "\nAutoModel classes practical completed successfully.")
        write_line(file, f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
