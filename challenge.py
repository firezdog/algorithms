from timeit import default_timer as timer
import random
import sys


def find_missing_numbers(numbers):
    # Given an array of integers, find the sum of the missing integers in the array.
    lo = numbers[0]
    hi = numbers[0]
    numbers = set(numbers)  # remove duplicates -- strategy 1 (strategy 2 is to use a dictionary, but it's slower)
    _sum = 0
    for number in numbers:
        if lo > number:
            lo = number
        if hi < number:
            hi = number
        _sum += number
    _range = hi - lo
    total_for_range = sum_from_one_to_n(hi) - sum_from_one_to_n(lo - 1)
    return total_for_range - _sum


def sum_from_one_to_n(n):
    return n * (n + 1) / 2


def doubling_test():
    limit = 1
    print("{}: {} -- {}".format("# entries", "sum of missing", "time"))
    print("====================================")
    while True:
        limit *= 2
        input_numbers = [random.randint(-9999999, 99999999) for iter in range(limit)]
        start = timer()
        missing = find_missing_numbers(input_numbers)
        end = timer()
        print("{}: {} -- {}s".format(limit, missing, end - start))


def user_input():
    input_numbers = input("Enter a list of numbers separated by spaces\n")
    try:
        processed_numbers = list(map(int, input_numbers.split(' ')))
        print(find_missing_numbers(processed_numbers))
    except Exception as e:
        print(e)


if __name__ == "__main__":
    commands = iter(sys.argv)
    arg_dict = dict(zip(range(len(sys.argv)), commands))
    if arg_dict.get(1, None) == "dt":
        doubling_test()
    else:
        user_input()
