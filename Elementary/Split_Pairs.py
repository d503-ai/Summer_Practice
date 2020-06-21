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