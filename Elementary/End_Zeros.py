def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))