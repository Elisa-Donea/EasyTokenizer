from PreTokenizer import tokenize_words
from bpe_core import train, tokenize

def tokenize(text: str) -> list[str]: 
    tokenized_list = tokenize_words(text)
    #utf8_words = [item.encode("utf-8") for item in tokenized_list]
    #utf8_tokens = train(utf8_words)

    temp = train(tokenized_list)

    return tokenize_words(text)
