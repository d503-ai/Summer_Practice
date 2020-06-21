def checkio(array: list) -> int:
    result = 0
    if array:
        for i in range(len(array)):
            if i % 2 == 0:
                result += array[i]
        return result * array[-1]
    else:
        return 0