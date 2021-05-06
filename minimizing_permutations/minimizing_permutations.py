def reverse(input_string):
    '''wrapper around python string slicing to reverse a string'''
    return input_string[::-1]

def generate_permutations(input_string):
    '''given a string, generate all permutations of that string that arise from reversing the order of sub-segments'''
    permutations = []
    segment_length = 2
    l = len(input_string)
    while segment_length <= len(input_string):
        for i, e in enumerate(input_string):
            sub_post = input_string[i+segment_length:]
            sub_pre = input_string[0:i]
            reversendum = input_string[i:i+segment_length]
            if len(reversendum) < segment_length: break
            permutations.append(sub_pre + reverse(reversendum) + sub_post)
        segment_length += 1
    return permutations

def min_operations(arr):
    '''
    arr is an array of integers of 1 to N, 1 < N < 8
    '''
    pass

print(generate_permutations('12345678'))