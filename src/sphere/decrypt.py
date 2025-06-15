def decrypt(mapping_data: dict[str, str | int], text: str) -> str:
    """Decrypt a given text using a mapping loaded from a JSON file.

    Args:
        mapping_data (dict[str, str | int]):
            The mapping dictionary containing character replacements.
        text (str): The input text to be decrypted.

    Returns:
        str: The decrypted text.
    """
    reversed_mapping = reverse_mappging(mapping_data)

    decrypted = [reversed_mapping.get(ch, "*") for ch in text.split()]
    result = "".join(decrypted)
    return result


def reverse_mappging(
    mapping_data: dict[str, str | int],
) -> dict[str, str | int]:
    """Reverse the keys and values in a mapping dictionary.

    Args:
        mapping_data (dict[str, str  |  int]): The original mapping dictionary.

    Returns:
        dict[str, str | int]: A new dictionary with keys and values reversed.
    """
    return {v: k for k, v in mapping_data.items()}
