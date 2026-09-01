import re

_SENTENCE_BOUNDARY = re.compile(r"(?<=[.!?])\s+")
_TOKEN_BOUNDARY = re.compile(r"(\s*)(\w+(?:'\w+)*|[^\w\s])")

def tokenize_words(text: str) -> list[str]:
    stripped = text.strip()
    if not stripped:
        return []

    raw_sentences = _SENTENCE_BOUNDARY.split(stripped)
    sentences = [s.strip() for s in raw_sentences if s.strip()]
    tokens = []
    for s in sentences:
        for match in _TOKEN_BOUNDARY.finditer(s):
            leading_ws, piece = match.group(1), match.group(2)
            tokens.append("Ġ" + piece if leading_ws else piece)
    return tokens
