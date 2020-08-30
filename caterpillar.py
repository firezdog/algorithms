from typing import List
import sys, traceback
'''
Check whether A[int] contains a contiguous sub-sequence of elements that sum to s.

Solution: use the "caterpillar" method (https://codility.com/media/train/13-CaterpillarMethod.pdf) -- pick a candidate to start the sub-sequence, then move through the array, gradually increasing the sub-sequence, keeping track of its sum.  As long as 

    sum <= s

we try to increase the size of the sub-sequence.  When we we overshoot the sum, we cancel growth and check our result.  If 

    total = s, 

we found the sub-sequence.  Otherwise, we should restart the sequence from the next item, adjusting the sum.
'''
def caterpillar(A: List[int], target: int):
    n = len(A)
    if not n:
        return False
    back, front, total = 0, 0, A[0]
    while front < n and back < n:
        if total < target:
            front += 1
            total += A[front] if front < n else 0
        if total == target:
            return True
        if total > target:
            if back < n:
                total -= A[back]
                back += 1
    return False

if __name__ == '__main__':
    A = list(map(lambda x: int(x), sys.argv[1].split(' ')))
    t = int(sys.argv[2])
    print(caterpillar(A, t))