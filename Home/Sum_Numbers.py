def sum_numbers(text: str) -> int:
    return sum(int(s) for s in text.split() if s.isdigit())