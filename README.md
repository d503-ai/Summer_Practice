# Projects from https://py.checkio.org/group/khai/ during summer practice time.

My tasks:

- [x] Complete Elementary projects;
- [x] Learn how to GitHub.
- [ ] Complete Home projects;

***Code of projects placed under exercise name or in separated files*** 

Completed projects:

## Elementary
- [x] Multiply (Intro);
```Python
def mult_two(a: int, b: int) -> int:
    return a*b
```
- [x] Easy Unpack.
```Python
def easy_unpack(elements: tuple) -> tuple:
    result = (elements[0], elements[2], elements[len(elements)-2])
    return result
```
- [x] First Word
```Python
def first_word(text: str) -> str:
    return text.split()[0]
```
- [x] Acceptable Password I
```Python
def is_acceptable_password(password: str) -> bool:
    return len(password) > 6
```
- [x] Number length
```Python
import math
def number_length(a: int) -> int:
    return int(math.log10(a)) + 1 if a else 1
```
- [x] End Zeros
```Python
def end_zeros(num: int) -> int:
    return len(s := str(num)) - len(s.rstrip('0'))
```
- [x] Backward string
```Python
def backward_string(val: str) -> str:
    return ''.join(reversed(val))
```
- [x] Remove All Before 
```Python
def remove_all_before(items: list, border: int) -> Iterable:
    try:
        return items[items.index(border):]
    except ValueError:
        return items
```
- [x] All Upper I
```Python
def is_all_upper(text: str) -> bool:
        if any(c.islower() for c in text):
            return False
        else:
            return True
```
- [x] Replace First
```Python
def replace_first(items: list) -> Iterable:
    if items:
        items += [items.pop(0)]
    return items
```
- [x] Max Digit
```Python
def max_digit(number: int) -> int:
    return int(max(str(number)))
```
- [x] Split Pairs
```Python
from textwrap import wrap
def split_pairs(a):
    if a:
        if len(a)%2 == 0:
            return wrap(a, 2)
        else:
            a += '_'
            return wrap(a, 2)
    else:
        return a
```
- [x] Beggining Zeros
```Python
def beginning_zeros(number: str) -> int:
    return len(number) - len(number.lstrip('0'))
```
- [x] Nearest Value
```Python
def nearest_value(values: set, one: int) -> int:
    return min(values, key=lambda x: (abs(one - x), x))
```
- [x] Between Markers
```Python
def between_markers(text: str, begin: str, end: str) -> str:
    return text[text.index(begin)+1:text.index(end)]
```
- [x] Correct Sentence
```Python
def correct_sentence(text: str) -> str:
    string = text[0].upper() + text[1:]
    if string[-1] != ".":
        string += "."
    return string
```
- [x] Is Even
```Python
def is_even(num: int) -> bool:
    return (True if num % 2 == 0 else False)
```
## Home
- [x] Sum Numbers
```Python
def sum_numbers(text: str) -> int:
    return sum(int(s) for s in text.split() if s.isdigit())
```
- [x] Even the Last
```Python
def checkio(array: list) -> int:
    result = 0
    if array:
        for i in range(len(array)):
            if i % 2 == 0:
                result += array[i]
        return result * array[-1]
    else:
        return 0
```
