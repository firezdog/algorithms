from functools import reduce

def find_max_product(arr):
    largest = [1, 1, 1]
    output = []

    for idx, item in enumerate(arr):
        # not sure if this is the cleanest implementation -- might be a recursive implementation that generalizes
        if item < largest[0]:
            if item <= largest[1]:
                largest[0] = largest[1]
                largest[1] = item
        if item > largest[0]:
            if item >= largest[2]:
                largest[0] = largest[1]
                largest[1] = largest[2]
                largest[2] = item

        if idx < 2:
            output.append(-1)
        else:
            output.append(reduce(lambda acc, x: acc * x, largest))

    return output

find_max_product([1,2,3,4,5,6])