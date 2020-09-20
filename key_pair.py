# Description:
# Given an array A of N positive integers and another number X.
# Determine whether or not there exist two elements in A whose sum is exactly X.
#
# Approach:
#
#
# Reference:
# https://https://www.geeksforgeeks.org/given-an-array-a-and-a-number-x-check-for-pair-in-a-with-sum-as-x/
#
# Complexity:
# O(n^2)

def key_pair(arr, sum_of_pair):
    """Prints all pairs in arr[] with given sum """
    from pandas import np
    n = len(arr)
    output_array = []
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == sum_of_pair:
                output_array.append([arr[i], arr[j]])
    return len(output_array)


assert key_pair([1, 4, 45, 6, 10, 8], 16) == 1
assert key_pair([1, 2, 4, 3, 6], 10) == 1