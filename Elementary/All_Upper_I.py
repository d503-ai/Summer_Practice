def is_all_upper(text: str) -> bool:
    if any(c.islower() for c in text):
        return False
    else:
        return True