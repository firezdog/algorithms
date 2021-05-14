from functools import reduce

def find_max_product(arr):
    largest = [-1, -1, -1]
    output = []

    for item in arr:
        product = reduce(lambda acc, curr: acc * curr, largest)
        print(product)

find_max_product([1,2,1,2])