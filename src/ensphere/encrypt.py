import unicodedata


def encrypt(codebook: dict[str, str | int], text: str) -> str:
    """Encrypt a given text using a mapping loaded from a JSON file.

    Args:
        codebook (dict[str, str | int]):
            The mapping dictionary containing character replacements.
        text (str): The input text to be encrypted.

    Returns:
        str: The encrypted text.
    """
    target = normalize_input(text)

    encrypted = [codebook.get(ch, "*") for ch in target]
    result = " ".join(str(x) for x in encrypted)
    return result


def normalize_input(text: str) -> str:
    """Convert text to a standardized format for encrypt.

    Args:
        text (str): The input text to be converted.

    Returns:
        str: The converted text in a standardized format.
    """
    return unicodedata.normalize("NFKC", text.lower())
