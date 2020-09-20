# Description:
# Given an array A[] of N numbers and another number x,
# determine whether or not there exist three elements in A[] whose sum is exactly x.
#
# Approach:
#
#
# Reference:
# https://https://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
#
# Complexity:
# O(n^3)

def triplet_sum_array(arr, sum_of_triplet):
    """Prints all triplets in arr[] with given sum """
    from pandas import np
    n = len(arr)
    output_array = []
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == sum_of_triplet:
                    row_to_be_added = [arr[i], arr[j], arr[k]]
                    output_array.append(row_to_be_added)
    return len(output_array)


assert triplet_sum_array([1, 4, 45, 6, 10, 8], 13) == 1
assert triplet_sum_array([1, 2, 4, 3, 6], 10) == 1
