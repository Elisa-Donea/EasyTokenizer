import re
_CHAR_SPLIT = re.compile(r".")
def tokenize(text: list[str]) -> list[str]:
    return text

def train(text: list[str]) -> list[str]:

    word_freq = {}
    for item in text: 
        if item not in word_freq:
            word_freq[item] = 1;
        else:
           word_freq[item] = word_freq[item] + 1
    print(word_freq)

    #de-duplicate
    text = list(set(text))
    print(word_freq)
    print(text)

    #split each character
    splits = {}

    print(splits)


    return text