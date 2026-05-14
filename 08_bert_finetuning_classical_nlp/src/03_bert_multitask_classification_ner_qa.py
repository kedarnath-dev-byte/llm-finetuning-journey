"""
Educational multi-task BERT fine-tuning skeleton.

This script explains how BERT can be adapted for:
1. Text Classification
2. Named Entity Recognition
3. Question Answering

Recommended:
- Use Colab GPU for actual training.
- Use this file as clean GitHub proof of architecture understanding.

Note:
This is a structured learning script, not a heavy production trainer.
"""

from dataclasses import dataclass


@dataclass
class BertTaskInfo:
    task_name: str
    huggingface_model_class: str
    expected_input_format: str
    expected_output_format: str
    example_business_use_case: str


def get_bert_task_catalog():
    return [
        BertTaskInfo(
            task_name="Text Classification",
            huggingface_model_class="BertForSequenceClassification",
            expected_input_format="One text/document with one label",
            expected_output_format="Single class label",
            example_business_use_case="Classify customer reviews as positive or negative",
        ),
        BertTaskInfo(
            task_name="Named Entity Recognition",
            huggingface_model_class="BertForTokenClassification",
            expected_input_format="Text where each token has an entity label",
            expected_output_format="Label for each token",
            example_business_use_case="Extract names, locations, skills, medicines, or legal entities",
        ),
        BertTaskInfo(
            task_name="Question Answering",
            huggingface_model_class="BertForQuestionAnswering",
            expected_input_format="Question plus context passage",
            expected_output_format="Start and end span of the answer inside the context",
            example_business_use_case="Answer questions from policy, legal, HR, or academic documents",
        ),
    ]


def explain_task(task: BertTaskInfo) -> None:
    print("=" * 80)
    print(f"Task: {task.task_name}")
    print(f"Hugging Face model class: {task.huggingface_model_class}")
    print(f"Expected input format: {task.expected_input_format}")
    print(f"Expected output format: {task.expected_output_format}")
    print(f"Business use case: {task.example_business_use_case}")


def main():
    print("BERT Multi-Task Fine-Tuning Architecture")
    print("Same BERT encoder, different task-specific heads.")
    print()

    for task in get_bert_task_catalog():
        explain_task(task)

    print("=" * 80)
    print("Memory Line:")
    print("BERT base gives language understanding. The task head decides the final task output.")


if __name__ == "__main__":
    main()
