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


def binary_search(arr: List[int], sought: int) -> int:
    # assumes arr is sorted! non-recursive approach
    if not len(arr):
        return -1
    minimum: int = 0
    maximum: int = len(arr) - 1
    while minimum <= maximum:
        middle: int = math.floor((minimum + maximum) / 2)
        tested: int = arr[middle]
        if tested == sought:
            return middle
        if tested < sought:
            minimum = middle + 1
            continue
        if tested > sought:
            maximum = middle - 1
            continue
    return -1


def number_of_ways(arr: List, k: int) -> int:
    sorted_arr: List[int] = sorted(arr)
    count: int = 0
    while len(sorted_arr) > 1:  # we can't have a pair of one element
        curr: int = sorted_arr.pop(0)
        sought: int = k - curr
        result: int = binary_search(sorted_arr, sought)
        if result >= 0:
            count += 1
            prev_result: int = result - 1
            next_result: int = result + 1
            # count backward to get duplicates before
            while prev_result >= 0 and sorted_arr[prev_result] == sought: 
                count += 1
                prev_result -= 1
            # count forward to get duplicates after
            while next_result < len(sorted_arr) and sorted_arr[next_result] == sought:
                count += 1
                next_result += 1
    return count