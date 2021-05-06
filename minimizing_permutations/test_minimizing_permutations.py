from minimizing_permutations import min_operations

def test_min_operations():
    arr = [1, 2, 5, 4, 3]
    assert min_operations(arr) == 1

    arr = [3, 1, 2]
    assert min_operations(arr) == 2