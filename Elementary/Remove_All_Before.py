def remove_all_before(items: list, border: int) -> Iterable:
    try:
        return items[items.index(border):]
    except ValueError:
        return items