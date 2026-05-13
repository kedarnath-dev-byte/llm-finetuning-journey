"""
06_embeddings_and_similarity.py

Purpose:
Generate embeddings using Hugging Face AutoModel and Sentence Transformers.

Video Topic:
Embedding using AutoModel, cosine similarity, and Sentence Transformer

This script demonstrates:
1. Loading BERT tokenizer and base model
2. Creating tokenized model inputs
3. Extracting last_hidden_state
4. Creating sentence embedding using mean pooling
5. Calculating cosine similarity
6. Using SentenceTransformer for simpler sentence embeddings
7. Saving output proof for GitHub
"""

from pathlib import Path

import torch
from sklearn.metrics.pairwise import cosine_similarity
from transformers import AutoTokenizer, AutoModel
from sentence_transformers import SentenceTransformer


OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

OUTPUT_FILE = OUTPUT_DIR / "embeddings_and_similarity_output.txt"


def write_line(file, text: str = "") -> None:
    """
    Print output to terminal and save same output to file.
    """
    print(text)
    file.write(text + "\n")


def mean_pooling(last_hidden_state: torch.Tensor, attention_mask: torch.Tensor) -> torch.Tensor:
    """
    Converts token-level embeddings into one sentence-level embedding.

    last_hidden_state shape:
    [batch_size, sequence_length, hidden_size]

    attention_mask shape:
    [batch_size, sequence_length]

    Output shape:
    [batch_size, hidden_size]
    """
    expanded_mask = attention_mask.unsqueeze(-1).expand(last_hidden_state.size()).float()
    masked_embeddings = last_hidden_state * expanded_mask

    summed_embeddings = masked_embeddings.sum(dim=1)
    token_counts = expanded_mask.sum(dim=1).clamp(min=1e-9)

    sentence_embedding = summed_embeddings / token_counts
    return sentence_embedding


def get_bert_sentence_embedding(
    text: str,
    tokenizer: AutoTokenizer,
    model: AutoModel,
) -> torch.Tensor:
    """
    Creates a sentence embedding using BERT AutoModel and mean pooling.
    """
    encoded_input = tokenizer(
        text,
        padding=True,
        truncation=True,
        return_tensors="pt",
    )

    with torch.no_grad():
        model_output = model(**encoded_input)

    sentence_embedding = mean_pooling(
        model_output.last_hidden_state,
        encoded_input["attention_mask"],
    )

    return sentence_embedding


def main() -> None:
    with OUTPUT_FILE.open("w", encoding="utf-8") as file:
        write_line(file, "=" * 80)
        write_line(file, "Embeddings and Cosine Similarity")
        write_line(file, "=" * 80)

        sentence_1 = "Hugging Face helps developers build AI applications."
        sentence_2 = "Hugging Face provides tools for machine learning developers."
        sentence_3 = "The farmer is checking crop disease in the field."

        write_line(file, "\nSentences used:")
        write_line(file, f"Sentence 1: {sentence_1}")
        write_line(file, f"Sentence 2: {sentence_2}")
        write_line(file, f"Sentence 3: {sentence_3}")

        model_name = "bert-base-uncased"

        write_line(file, f"\nLoading tokenizer and AutoModel: {model_name}")
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModel.from_pretrained(model_name)
        model.eval()

        write_line(file, "\nGenerating BERT AutoModel embeddings using mean pooling...")

        embedding_1 = get_bert_sentence_embedding(sentence_1, tokenizer, model)
        embedding_2 = get_bert_sentence_embedding(sentence_2, tokenizer, model)
        embedding_3 = get_bert_sentence_embedding(sentence_3, tokenizer, model)

        write_line(file, f"Embedding 1 shape: {tuple(embedding_1.shape)}")
        write_line(file, f"Embedding 2 shape: {tuple(embedding_2.shape)}")
        write_line(file, f"Embedding 3 shape: {tuple(embedding_3.shape)}")

        sim_1_2 = cosine_similarity(embedding_1.numpy(), embedding_2.numpy())[0][0]
        sim_1_3 = cosine_similarity(embedding_1.numpy(), embedding_3.numpy())[0][0]

        write_line(file, "\nCosine similarity using BERT AutoModel + mean pooling:")
        write_line(file, f"Similarity(sentence_1, sentence_2): {sim_1_2:.4f}")
        write_line(file, f"Similarity(sentence_1, sentence_3): {sim_1_3:.4f}")

        write_line(file, "\nInterpretation:")
        write_line(
            file,
            "Sentence 1 and Sentence 2 are both about Hugging Face/AI tools, so their similarity should be higher."
        )
        write_line(
            file,
            "Sentence 3 is about agriculture, so it should be less similar to Sentence 1."
        )

        write_line(file, "\n" + "-" * 80)
        write_line(file, "SentenceTransformer Embeddings")
        write_line(file, "-" * 80)

        sentence_transformer_model_name = "sentence-transformers/all-MiniLM-L6-v2"
        write_line(file, f"\nLoading SentenceTransformer model: {sentence_transformer_model_name}")

        sentence_model = SentenceTransformer(sentence_transformer_model_name)

        sentences = [sentence_1, sentence_2, sentence_3]
        st_embeddings = sentence_model.encode(sentences)

        write_line(file, f"SentenceTransformer embeddings shape: {st_embeddings.shape}")

        st_sim_1_2 = cosine_similarity([st_embeddings[0]], [st_embeddings[1]])[0][0]
        st_sim_1_3 = cosine_similarity([st_embeddings[0]], [st_embeddings[2]])[0][0]

        write_line(file, "\nCosine similarity using SentenceTransformer:")
        write_line(file, f"Similarity(sentence_1, sentence_2): {st_sim_1_2:.4f}")
        write_line(file, f"Similarity(sentence_1, sentence_3): {st_sim_1_3:.4f}")

        write_line(file, "\nProduction learning:")
        write_line(
            file,
            "AutoModel gives token-level hidden states and requires pooling to create sentence embeddings."
        )
        write_line(
            file,
            "SentenceTransformer is easier for semantic similarity because it is trained specifically for sentence embeddings."
        )
        write_line(
            file,
            "These embeddings are useful for RAG, semantic search, recommendations, clustering, and document similarity."
        )

        write_line(file, "\nEmbeddings and similarity practical completed successfully.")
        write_line(file, f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
