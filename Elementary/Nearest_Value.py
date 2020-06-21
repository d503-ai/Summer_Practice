def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda x: (abs(one - x), x))