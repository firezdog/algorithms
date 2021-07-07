from pair_sum import binary_search, number_of_ways

def test_binary_search():
    test_array = [1, 2, 2, 5, 7, 7, 8, 10]

    assert binary_search(test_array, 1) == 0
    assert binary_search(test_array, 10) == 7
    assert binary_search(test_array, 7) == 4 or 5
    assert binary_search(test_array, 11) == -1
    assert binary_search(test_array, 0) == -1
    assert binary_search(test_array, 4) == -1


def test_num_ways():
    arr = [1, 2, 3, 4, 3]
    sought = 6
    assert number_of_ways(arr, sought) == 2

    arr = [1, 5, 3, 3, 3]
    sought = 6
    assert number_of_ways(arr, sought) == 4

    arr = [1, 1, 1, 1]
    sought = 2
    assert number_of_ways(arr, sought) == 6

    arr = [0, 3, -3, 6]
    sought = 3
    assert number_of_ways(arr, sought) == 2