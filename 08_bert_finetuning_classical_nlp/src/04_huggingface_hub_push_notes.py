"""
Hugging Face Hub push workflow notes.

This file documents the safe steps to push a fine-tuned BERT model
to Hugging Face Hub after training.

Important:
Never hardcode Hugging Face tokens inside Python files or GitHub repo.
Use notebook_login(), huggingface-cli login, or environment variables.
"""


def print_hub_push_workflow():
    print("Safe Hugging Face Hub Push Workflow")
    print("=" * 70)

    print("\n1. Train and save the model:")
    print("trainer.save_model('outputs/bert_finetuned_imdb')")
    print("tokenizer.save_pretrained('outputs/bert_finetuned_imdb')")

    print("\n2. Login safely in Colab:")
    print("from huggingface_hub import notebook_login")
    print("notebook_login()")

    print("\n3. Push tokenizer:")
    print("tokenizer.push_to_hub('your-username/bert-imdb-sentiment-classifier')")

    print("\n4. Push model:")
    print("model.push_to_hub('your-username/bert-imdb-sentiment-classifier')")

    print("\n5. Load later:")
    print("from transformers import pipeline")
    print("classifier = pipeline('text-classification', model='your-username/bert-imdb-sentiment-classifier')")

    print("\nSecurity Notes:")
    print("- Do not commit access tokens.")
    print("- Use write token only when pushing.")
    print("- Use read token for private loading.")
    print("- Avoid pushing private company/client data.")
    print("- Create model card with dataset, task, limitations, and evaluation details.")


if __name__ == "__main__":
    print_hub_push_workflow()
