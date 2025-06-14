import json
import os
import unicodedata


def encrypt(text: str) -> str:
    """Encrypt a given text using a mapping loaded from a JSON file.

    Args:
        text (str): The input text to be encrypted.

    Returns:
        str: The encrypted text, where each character is replaced according to the mapping.
    """
    mapping = load_mapping()
    mapping_lower = {k.lower(): v for k, v in mapping.items()}

    target = normalize_input(text)

    encrypted = [mapping_lower.get(ch, "*") for ch in target]
    result = " ".join(str(x) for x in encrypted)
    return result


def load_mapping() -> dict[str, str | int]:
    """Load the mapping from a JSON file.

    Raises:
        FileNotFoundError: mapping file not found at the specified path.
        Exception: An error occurred while loading the mapping.

    Returns:
        dict[str, str | int]: A dictionary containing the mapping from the JSON file.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    mapping_file_path = os.path.join(BASE_DIR, "mapping", "mapping.json")

    try:
        with open(mapping_file_path, "r") as file:
            mapping = json.load(file)
        return mapping
    except FileNotFoundError:
        raise FileNotFoundError(f"Mapping file not found at {mapping_file_path}")
    except Exception as e:
        raise Exception(e)


def normalize_input(text: str) -> str:
    """Convert text to a standardized format for encrypt.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The converted text in a standardized format.
    """
    return unicodedata.normalize("NFKC", text.lower())
