def two_sum(lst, k):
    complements = set()
    for x in lst:
        if x in complements:
            return True
        complements.add(k-x)
    return False


if __name__ == "__main__":
    print(two_sum([10, 15, 3, 7], 17))
    print(two_sum([10, 15, 3, 7], 25))
    print(two_sum([10, 15, 3, 7], 20))


