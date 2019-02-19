"""
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

"""


"""
Observation: Solution will be in [1, ... n+1] where n is len(lst)

Solution:
    - Let each index i represent if i+1 is seen, turn negative if seen
    - Since we can have negatives in the list, need some way to partition
    negative/positive - Partition between positive [0...end]
    and non-positive [end+1...n-1]

    New Observation: Solution between [1, ... end+2] (since end is an index)
    - Search through new positive array, mark elements which are seen
    - Return smallest such index that wasn't seen yet
"""


def partition(lst):
    """
        args: lst --> list of integers
        returns: number of positive elements (num_pos)
    """
    def swap(i, j):
        tmp = lst[i]
        lst[i] = lst[j]
        lst[j] = tmp

    num_pos = 0
    for i in range(len(lst)):
        if lst[i] > 0:
            swap(i, num_pos)
            num_pos += 1
    return num_pos


def find_missing_pos(lst):
    num_pos = partition(lst)

    # First pass, mark if visited. Need to offset by -1 since we need to map
    # the values to be zero-indexed
    for i in range(num_pos):
        # Check if the value is positive and within the range
        if lst[i] > 0 and lst[i] - 1 < num_pos:
            # Mark as negative
            lst[lst[i] - 1] *= -1

    # Second pass: Return i+1 such that lst[i] is positive
    for i in range(num_pos):
        if lst[i] > 0:
            return i+1
    return num_pos + 1


if __name__ == "__main__":
    # Expected: 1
    print(find_missing_pos([3, 4, -1, 1]))

    # Expected: 3
    print(find_missing_pos([1, 2, 0]))
