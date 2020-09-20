# Description:
# An array is called Bitonic if it is comprises of an increasing sequence of integers
# followed immediately by a decreasing sequence of integers.
# Given a bitonic array A of N distinct integers. Find a element X in it.
#
# Approach:
#
#
# Reference:
# https://www.geeksforgeeks.org/find-bitonic-point-given-bitonic-sequence/
#
# Complexity:
# O(n)

def find_number_bitonic(num, k):
    """ Find the element ``p`` in a bitonic array where the entries
    switch from strictly increasing to strictly decreasing."""

    size = len(num)
    for i in range(size):
        if num[i] == k:
            return i
    return -1


assert find_number_bitonic([1, 2, 7, 4, 3], 2) == 1
