import math
def number_length(a: int) -> int:
    return int(math.log10(a)) + 1 if a else 1