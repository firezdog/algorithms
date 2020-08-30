from typing import List
import sys, traceback
'''
Check whether A[int] contains a contiguous sub-sequence of elements that sum to s.

Solution: use the "caterpillar" method (https://codility.com/media/train/13-CaterpillarMethod.pdf), more commonly known as double-index method.  We keep two pointers to the head and tail of the sub-sequence.  As long as the pointers are within the array, we increase one or the other depending on whether we have exceeded the target sum.  If our sum is lower than the target, we add to the front -- with the result that the sum of our sub-sequence increases.  If our sum is greater than the target, we add to the back -- with the result that the sum of our sub-sequence decreases.  We return True when we reach the target; if we exceed the bounds of the array without reaching the target, we return false.  (If we sum over the whole array and never reach our target, front will increase and back will remain in place...

TODO: apparently this will not work with negative numbers / negative sums)?
'''
def caterpillar(A: List[int], target: int):
    n = len(A)
    if not n:
        return False
    back, front, total = 0, 0, A[0]
    while front < n and back < n:
        print(back, front)
        if total < target:
            front += 1
            if front < n:
                total += A[front]
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