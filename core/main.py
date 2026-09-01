import sys

from Tokenizer import tokenize

_instruction = "enter text, press Ctrl+Z then Enter to tokenize"

def main() -> None:

    #text = _read_input()
    text = "hello. my name is, Bob!!! Isn't that amazing?"

    tokens = tokenize(text)
    _print_tokens(tokens)

def _read_input() -> str:
    print(_instruction)
    return sys.stdin.read()

def _print_tokens(tokens: list[str]) -> None:
        print(f"{tokens}")

if __name__ == "__main__":
    main()