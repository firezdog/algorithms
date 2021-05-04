from contiguous_subarrays import count_left, count_right, count_subarrays

class Test_Contiguous_Subarrays():
    def test_count_right(self):
        assert count_right(0, 3, [3, 2, 5]) == 1
        assert count_right(1, 2, [3, 2, 5]) == 0
        assert count_right(2, 5, [3, 2, 5]) == 0
    
    def test_count_left(self):
        assert count_left(0, 3, [3, 2, 5]) == 0
        assert count_left(1, 2, [3, 2, 5]) == 0
        assert count_left(2, 5, [3, 2, 5]) == 2
    
    def test_count_subarrays(self):
        assert count_subarrays([3, 2, 5]) == [2, 1, 3]
        assert count_subarrays([2, 4, 7, 1, 5, 3]) == [1, 2, 6, 1, 3, 1]
        assert count_subarrays([3, 4, 1, 6, 2]) == [1, 3, 1, 5, 1]