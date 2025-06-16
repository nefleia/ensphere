import json
import os


def get_codebook() -> dict[str, str | int]:
    """Get the codebook from a JSON file.

    Returns:
        dict[str, str | int]:
            A dictionary containing the codebook from the JSON file.
    """
    original_codebook = _load_codebook_json()
    _validate_codebook(original_codebook)

    return _lower_codebook(original_codebook)


def _load_codebook_json() -> dict[str, str | int]:
    """Load the codebook from a JSON file.

    Raises:
        FileNotFoundError: codebook file not found at the specified path.
        Exception: An error occurred while loading the codebook.

    Returns:
        dict[str, str | int]:
            A dictionary containing the codebook from the JSON file.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    codebook_file_path = os.path.join(BASE_DIR, "codebook", "codebook.json")

    try:
        with open(codebook_file_path, "r") as file:
            codebook = json.load(file)
        return codebook
    except FileNotFoundError:
        raise FileNotFoundError("codebook file not found")
    except Exception as e:
        raise Exception(e)


def _validate_codebook(codebook: dict[str, str | int]) -> None:
    """Validate the codebook.

    Args:
        codebook (dict[str, str | int]): The codebook dictionary to validate.

    Raises:
        ValueError: If the codebook contains a '*' key.
    """
    if "*" in codebook:
        raise ValueError("'*' key is not allowed in the codebook.")


def _lower_codebook(codebook: dict[str, str | int]) -> dict[str, str | int]:
    """Convert all keys in the codebook to lowercase.

    Args:
        codebook (dict[str, str | int]): The original codebook dictionary.

    Returns:
        dict[str, str | int]:
            A new dictionary with all keys converted to lowercase.
    """
    return {k.lower(): v for k, v in codebook.items()}
