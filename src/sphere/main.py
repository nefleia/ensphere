import argparse

from sphere import mapping
from sphere.decrypt import decrypt
from sphere.encrypt import encrypt


def main():
    parser = argparse.ArgumentParser(
        description="Encrypt or decrypt a string."
    )
    parser.add_argument(
        "mode", choices=["encrypt", "decrypt"], help="Mode: encrypt or decrypt"
    )
    args = parser.parse_args()

    try:
        mapping_data = mapping.get_mapping()
        print("Enter text to encrypt (or 'exit' to quit):")

        while True:
            text = input(">> ")
            if text.lower() == "exit":
                break

            if args.mode == "encrypt":
                result = encrypt(mapping_data, text)
            else:
                result = decrypt(mapping_data, text)

            print(result)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
