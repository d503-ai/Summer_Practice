def first_word(text: str) -> str:
    text = text.replace('.', ' ').replace(',', ' ').strip()
    return text.split()[0]