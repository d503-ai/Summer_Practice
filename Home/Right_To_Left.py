def left_join(phrases: tuple) -> str:
    result = [i.replace("right", "left") for i in phrases]
    return ','.join(result)