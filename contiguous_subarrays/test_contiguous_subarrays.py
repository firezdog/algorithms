from contiguous_subarrays import (
    count_left, 
    count_right, 
    count_subarrays,
    get_local_maxima,
)

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
    
    def test_maxima(self):
        test_array = [2, 4, 7, 1, 5, 3]
        result_left = get_local_maxima([2, 4, 7, 1, 5, 3])

        assert len(result_left) == 3
        
        assert result_left[0].element == 3
        assert result_left[0].position == 5
        assert result_left[0].count == 0

        assert result_left[1].element == 5
        assert result_left[1].position == 4
        assert result_left[1].count == 1

        assert result_left[2].element == 7
        assert result_left[2].position == 2
        assert result_left[2].count == 2

        result_right = get_local_maxima([2, 4, 7, 1, 5, 3], False)

        assert len(result_right) == 3

        assert result_right[0].element == 2
        assert result_right[0].position == 0
        assert result_right[0].count == 0

        assert result_right[1].element == 4
        assert result_right[1].position == 1
        assert result_right[1].count == 0

        assert result_right[2].element == 7
        assert result_right[2].position == 2
        assert result_right[2].count == 3