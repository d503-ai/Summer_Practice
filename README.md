# Projects from https://py.checkio.org/group/khai/ during summer practice time.

My tasks:

- [ ] Complete Elementary projects;
- [x] Learn how to GitHub.

***Code of projects placed under exercise's name*** 

Completed projects:

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
