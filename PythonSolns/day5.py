"""
cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Implement car and cdr
"""


def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# car returns the first element of a pair
def car(pair):
    def first(a, b):
        return a
    return pair(first)


# cdr returns the second element of a pair
def cdr(pair):
    def rest(a, b):
        return b
    return pair(rest)


if __name__ == "__main__":
    # Expected: 3
    print(car(cons(3, 4)))

    # Expected: 4
    print(cdr(cons(3, 4)))
