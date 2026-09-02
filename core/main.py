from Tokenizer import tokenize

def main() -> None:

    text = "hello. hello, low low lower lowest. hi."

    tokens = tokenize(text)
    #_print_tokens(tokens)


def _print_tokens(tokens: list[str]) -> None:
        print(f"{tokens}")

if __name__ == "__main__":
    main()