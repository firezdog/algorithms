'''
Contiguous Sub-Arrays

Given an array, for each item, how many sub-arrays formed from elements to the left and right of that item includes that item as the largest element?

This question seems to be asking, for each element, how many elements that element is larger than to its left and how many elements that element is larger than to its right.  This ++ (for the element itself would be the answer).

Ex. [3, 4, 1, 6, 2]

3 is only the greatest for [3] (its singleton) and has nothing to the left
it is not greater than anything to the right => 1

4 is greater than 1 element to the left (3) and 1 element to the right (1) (contiguity limits so that e.g. 2 doesn't count) => 1 left + 1 right + 1 = 3

1 is greater neither than 4 nor 6 => 1

6 (1) is greater than 1, 4, 3 to the left (3) and 2 to the right (1) => 1 + 3 + 1 = 5

2 (1) is not greater than anything to the left and nothing to the right => 1

This works as a brute force approach, but seems like you get close to N * N in the worst case.

Note that if your array is ordered, the number for each element is just its position + 1, right?

It seems like if we create an ordered data structure that preserves original position, we can quickly determine.

How would that look? (Note our example has no duplicates)

1 (orig. 2)
2 (orig. 4)
3 (orig. 0)
4 (orig. 1)
6 (orig. 3)

We can immediately see the highest potential for 1 is 1 since it is the least element in this array

The potential for 2 is 1 but because 1's position is not contiguous...

So what if we somehow order the two arrays and do cross pointers?

*1 2 3 4 6
3 4 *1 6 2

we know it is 1 here

1 *2 3 4 6
3 4 1 6 *2

we know this has to be 1 because 2 is not next to 1 (prev 2 != 1, 2 has no next) -- but does this save us any time?

1 2 *3 4 6
*3 4 1 6 2

we know this has to be 1 because 2 is not next to 1

1 2 3 *4 6
3 *4 1 6 2

4 is next to 1 and 3...but how do we tell about 2?

1 2 3 4 *6
3 4 1 *6 2

we know 6 is the greatest so we don't really have to check...

Note: a more efficient approach using dynamic programming may be possible...

Idea for efficiency: note that if we're at some position p in the array, and we know a[p] > a[p-1], then everything that included a[p-1] as the greatest right-most can form a new sub-array with p as the greatest right-most -- similarly for the left.  So we have this:

[5, 3, 4, 7, 6, 3, 10]

For 4 we had [3, 4] and [4], so for 7 to the left we have [3, 4, 7], [4, 7], and then [7]
For 6 (to the right of 7) we had [6] and [6, 3], so for 7 for we [7], [7, 6], and [7, 6, 3]

Now we can really only calculate in advance to the left -- but we're sort of doing the work ahead of time when we calculate to the right.
'''

def count_left(pointer, element, array, left_result):
    curr = pointer - 1
    count = 0

    # use pre-computed values if the current element is greater than the last element
    # this doesn't seem to be working yet
    # previous = pointer - 1
    # next_result = 0
    # while previous >= 0 and element > array[previous]:
    #     next_result += left_result[previous]
    #     previous -= 1

    while curr >= 0:
        if element > array[curr]:
            count += 1
            curr -= 1
        else:
            break
    # left_result.append(next_result)

    return count

def count_right(pointer, element, array):
    curr = pointer + 1
    count = 0
    l = len(array)
    while curr < l:
        if element > array[curr]:
            count += 1
            curr += 1
        else:
            break
    return count

def count_subarrays(arr):
    result = []
    left_result = []
    for i, e in enumerate(arr):
        left = count_left(i, e, arr, left_result)
        right = count_right(i, e, arr)
        result.append(left + right + 1)
    return result