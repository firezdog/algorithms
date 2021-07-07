def slow_sums(arr):
    sorted_arr = sorted(arr)
    ops = []
    ops.append(sum(sorted_arr))
    last_op = ops[0]
    for item in sorted_arr[:-2]:    # why -2?  Not totally sure but I think b/c we leave a pair for the initial operation?
        last_op = last_op - item
        ops.append(last_op)
    print(ops)
    return sum(ops)

print(slow_sums([2,3,9,8,4]))