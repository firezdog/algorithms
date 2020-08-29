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
def caterpillar(A: List[int], s: int):
    front, total = 0, 0
    n = len(A)
    for back in range(n):
        if back + 1 < n:
            next_total = A[back + 1]
        while front < n:
            new_total = total + A[front]
            if new_total <= s:
                total = new_total
                front += 1
            else: break
        if total == s:
            return True
        total = next_total
    return False

if __name__ == '__main__':
    A = list(map(lambda x: int(x), sys.argv[1].split(' ')))
    t = int(sys.argv[2])
    print(caterpillar(A, t))