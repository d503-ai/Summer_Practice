def replace_first(items: list):
    if items:
        items += [items.pop(0)]
    return items