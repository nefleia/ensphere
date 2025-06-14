import json
import os


def get_mapping() -> dict[str, str | int]:
    """Get the mapping from a JSON file.

    Raises:
        FileNotFoundError: mapping file not found at the specified path.
        Exception: An error occurred while loading the mapping.

    Returns:
        dict[str, str | int]:
            A dictionary containing the mapping from the JSON file.
    """
    original_mapping = _load_mapping()
    validate_mapping(original_mapping)

    return _lower_mapping(original_mapping)


def _load_mapping() -> dict[str, str | int]:
    """Load the mapping from a JSON file.

    Raises:
        FileNotFoundError: mapping file not found at the specified path.
        Exception: An error occurred while loading the mapping.

    Returns:
        dict[str, str | int]:
            A dictionary containing the mapping from the JSON file.
    """
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    mapping_file_path = os.path.join(BASE_DIR, "mapping", "mapping.json")

    try:
        with open(mapping_file_path, "r") as file:
            mapping = json.load(file)
        return mapping
    except FileNotFoundError:
        raise FileNotFoundError("Mapping file not found")
    except Exception as e:
        raise Exception(e)


def validate_mapping(mapping: dict[str, str | int]) -> None:
    """Validate the mapping.

    Args:
        mapping (dict[str, str | int]): The mapping dictionary to validate.

    Raises:
        ValueError: If the mapping contains a '*' key.
    """
    if "*" in mapping:
        raise ValueError("'*' key is not allowed in the mapping.")


def _lower_mapping(mapping: dict[str, str | int]) -> dict[str, str | int]:
    """Convert all keys in the mapping to lowercase.

    Args:
        mapping (dict[str, str | int]): The original mapping dictionary.

    Returns:
        dict[str, str | int]:
            A new dictionary with all keys converted to lowercase.
    """
    return {k.lower(): v for k, v in mapping.items()}
