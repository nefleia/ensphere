from sphere import mapping
from sphere.encrypt import encrypt


def main():
    try:
        mapping_data = mapping.get_mapping()
        print("Enter text to encrypt (or 'exit' to quit):")

        while True:
            text = input(">> ")
            if text.lower() == "exit":
                break

            result = encrypt(mapping_data, text)
            print(result)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
