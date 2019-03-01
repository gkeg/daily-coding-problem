"""
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

# Possible solution: Get a product of all of them if there's no 0, divide by the number at that index


# Right and left list, multiply those together
def x_product(lst):

    # Step 1: Build the "left" list
    left_prod = 1
    n = len(lst)
    left_lst = [None] * n
    for i in range(n):
        left_lst[i] = left_prod
        left_prod *= lst[i]

    # Step 2: Build the "right" list
    right_prod = 1
    right_lst = [None] * n
    for i in reversed(range(n)):
        right_lst[i] = right_prod
        right_prod *= lst[i]

    # Step 3: Multiply them together
    res = []
    for i in range(n):
        res.append(right_lst[i] * left_lst[i])

    return res


# O(1) space solution
def x_product_opt(lst):
    prod = 1
    n = len(lst)
    res = [None] * n

    # Left side
    for i in range(n):
        res[i] = prod
        prod *= lst[i]

    # Right side
    prod = 1
    for i in reversed(range(n)):
        res[i] *= prod
        prod *= lst[i]

    return res


if __name__ == '__main__':
    # First implementation
    print(x_product([1, 2, 3, 4, 5]))
    print(x_product([3, 2, 1]))

    # Second implementation
    print(x_product_opt([1, 2, 3, 4, 5]))
    print(x_product_opt([3, 2, 1]))





