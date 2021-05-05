def efficient_count_left(pointer, element, array, left_result):
    ''' 
    the reason this does not work is that you can have "valleys":
    [3, 4, 1, 6, 2] @1 is a valley with 0 as left result, but 6 is greater than 4 to its left
    so really we need the result from 4
    this method can only save us from iterating over elements to the left of the highest hill smaller than the current element
    '''
    result = 0
    if pointer == 0:
        left_result[pointer] = result
        return result
    prev = pointer - 1
    if pointer > 0 and element > array[prev]:
        result = 1 + left_result[prev]
    
    left_result[pointer] = result
    return result
    

def count_left(pointer, element, array):
    curr = pointer - 1
    count = 0
    while curr >= 0:
        if element > array[curr]:
            count += 1
            curr -= 1
        else:
            break
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

class LocalMax():
    def __init__(self, element, position, count):
        self.element = element
        self.position = position
        self.count = count

def get_local_maxima(arr, left = True):
    '''
    given an array, returns a sub-array of local maxima 
        each element has as attributes 
            the maximum, 
            number of elements to its left than which it is greater
            position in the array
    '''
    maxima = []
    i = len(arr) - 1 if left else 0
    curr_max = arr[i]
    curr_max_i = i
    curr_max_count = 0
    while i > 0 if left else i < len(arr) - 1:
        next = arr[i - 1] if left else arr[i + 1]
        if curr_max > next: curr_max_count += 1
        else:
            maxima.append(LocalMax(
                curr_max, 
                curr_max_i,
                curr_max_count,
            ))
            curr_max = next
            curr_max_i = i - 1 if left else i + 1
            curr_max_count = 0
        i += (-1 if left else 1)
    maxima.append(LocalMax(
        curr_max, 
        curr_max_i,
        curr_max_count,
    ))
    return maxima

def count_subarrays(arr):
    result = [0] * len(arr)
    left_result = [0] * len(arr)
    for i, e in enumerate(arr):
        # left = efficient_count_left(i, e, arr, left_result)
        left = count_left(i, e, arr)
        right = count_right(i, e, arr)
        result[i] = left + right + 1
    return result