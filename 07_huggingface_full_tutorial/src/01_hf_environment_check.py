"""
01_hf_environment_check.py

Purpose:
This script checks whether the local environment is ready for Hugging Face hands-on practice.

Video Topic:
Hugging Face Full Tutorial for LLM Fine-Tuning Journey

What this proves:
- Python is working
- Hugging Face-related packages are installed
- PyTorch is available
- GPU availability is checked
"""

import sys
import importlib.util


def check_package(package_name: str, import_name: str | None = None) -> None:
    """
    Checks whether a Python package is installed.
    """
    module_name = import_name or package_name
    spec = importlib.util.find_spec(module_name)

    if spec is None:
        print(f"? {package_name} is NOT installed")
    else:
        print(f"? {package_name} is installed")


def main() -> None:
    print("=" * 70)
    print("Hugging Face Environment Check")
    print("=" * 70)

    print(f"\nPython version: {sys.version}")

    print("\nChecking required packages:\n")

    check_package("torch")
    check_package("transformers")
    check_package("datasets")
    check_package("evaluate")
    check_package("huggingface_hub")
    check_package("sentence-transformers", "sentence_transformers")
    check_package("sklearn", "sklearn")
    check_package("pandas")
    check_package("matplotlib")

    print("\nChecking PyTorch device:\n")

    try:
        import torch

        print(f"PyTorch version: {torch.__version__}")
        print(f"CUDA available: {torch.cuda.is_available()}")

        if torch.cuda.is_available():
            print(f"GPU name: {torch.cuda.get_device_name(0)}")
        else:
            print("Running on CPU. This is okay for this Hugging Face tutorial.")
    except Exception as error:
        print(f"Could not check PyTorch device. Error: {error}")

    print("\nEnvironment check completed.")


if __name__ == "__main__":
    main()
