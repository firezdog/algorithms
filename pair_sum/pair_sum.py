'''
Given an array and a number, find the number of pairs that sum

Brute force: look at all pairs in the array and report the number with that sum (no assumptions about input, O(n^2))
    keep a running count

Non-brute force: sort the array, then do a binary search for the number you require, 
    O(time to sort + binary search for each element)
    O(2* (n * log n))
    keep a running count
    optimization: we do not need to keep going when we get to some element e > k 
        or when we start finding sums larger than k
        this only works if we assume non-negative numbers -- which we can based on the problem spec

Potential complication: we don't want to use the same element twice, so it seems we need to pop elements off the array when testing
'''
from typing import List
import math


def binary_search(arr, sought):
    # assumes arr is sorted! non-recursive approach
    if not len(arr):
        return (False, 0)
    minimum = 0
    maximum = len(arr) - 1
    while minimum <= maximum:
        middle = math.floor((minimum + maximum) / 2)
        tested = arr[middle]
        if tested == sought:
            return (True, middle)
        if tested < sought:
            minimum = middle + 1
            continue
        if tested > sought:
            maximum = middle - 1
            continue
    return (False, middle)


def number_of_ways(arr: List, k):
    sorted_arr = sorted(arr)
    count = 0
    while len(sorted_arr) > 1:  # we can't have a pair of one element
        curr = sorted_arr.pop(0)
        sought = k - curr
        if sought < 0:
            pass
        elif sought == 0:
            count += 1
        else:
            next = 0
            next_arr = sorted_arr[next:]
            result = binary_search(next_arr, sought)
            while (result[0] and len(next_arr) > 2):
                count += int(result[0])
                next_arr = sorted_arr[result[1]:]
                result = binary_search(next_arr, sought)
    return count