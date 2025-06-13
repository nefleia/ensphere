from sphere.entrypt import encrypt


def main():
    print("Enter text to encrypt (or 'exit' to quit):")
    try:
        while True:
            text = input(">> ")
            if text.lower() == 'exit':
                break

            result = encrypt(text)
            print(result)

    except KeyboardInterrupt:
        pass
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
