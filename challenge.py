# Given an array, find the sum of the missing numbers in the array.


def find_missing_numbers(numbers):
    lo = numbers[0]
    hi = numbers[0]
    _sum = 0
    for number in numbers:
        if lo > number:
            lo = number
        if hi < number:
            hi = number
        _sum += number
    _range = hi - lo
    total_for_range = (hi * (hi + 1) / 2) - ((lo - 1) * lo / 2)
    return total_for_range - _sum


if __name__ == "__main__":
    while True:
        input_numbers = list(map(int, input().split(' ')))
        print(find_missing_numbers(input_numbers))
