def correct_sentence(text: str) -> str:
    string = text[0].upper() + text[1:]
    if string[-1] != ".":
        string += "."
    return string