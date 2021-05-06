def reverse(input_string):
    '''wrapper around python string slicing to reverse a string -- allows for a non-cheat implementation if this were desired'''
    return input_string[::-1]

def generate_sub_permutations(seed):
    '''given a string, generate all permutations of that string that arise from reversing the order of sub-segments of increasing size'''
    permutations = []
    segment_length = 2
    input_length = len(seed)
    while segment_length <= len(seed):
        for i, e in enumerate(seed):
            if (i + segment_length) > input_length: break
            sub_post = seed[i+segment_length:]
            sub_pre = seed[0:i]
            reversendum = seed[i:i+segment_length]
            permutations.append(sub_pre + reverse(reversendum) + sub_post)
        segment_length += 1
    return permutations

def generate_all_permutations(input_string):
    seen = {}
    sub_permutations = generate_sub_permutations(input_string)
    while (len(sub_permutations)):
        sub_permutation = sub_permutations.pop()
        seen[sub_permutation] = True
        next_sub_permutations = generate_sub_permutations(sub_permutation)
        for next_sub_permutation in next_sub_permutations:
            if not seen.get(next_sub_permutation): sub_permutations.append(next_sub_permutation)
    return seen

def min_operations(arr):
    '''
    arr is an array of integers of 1 to N, 1 < N < 8
    '''
    pass

result = generate_all_permutations('1234567')
print(len(result))