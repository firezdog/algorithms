def get_el_count_map(arr):
    el_count_map = {}
    for item in arr:
        item_count = el_count_map.get(item, 0)
        el_count_map[item] = item_count + 1
    return el_count_map

def get_el_count_list(el_count_map):
    return sorted(el_count_map.values(), reverse=True)

def get_min_set_size(el_count_list, half):
    sum = 0
    set_size = 0
    ptr = 0

    while sum < half:
        sum += el_count_list[ptr]
        set_size += 1
        ptr += 1
    
    return set_size


class Solution(object):
    def minSetSize(self, arr):
        half = len(arr) / 2
        """
        :type arr: List[int]
        :rtype: int
        """
        el_count_map = get_el_count_map(arr)
        el_count_list = get_el_count_list(el_count_map)
        return get_min_set_size(el_count_list, half)

print(Solution().minSetSize([3,3,3,3,5,5,5,2,2,7]))
print(Solution().minSetSize([7,7,7,7,7,7]))
print(Solution().minSetSize([1,9]))
print(Solution().minSetSize([1000,1000,3,7]))
print(Solution().minSetSize([1,2,3,4,5,6,7,8,9,10]))