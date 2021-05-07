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

def generate_permutation_graph(input_string):
    permutation_graph = {}
    sub_permutations = [input_string]
    while (len(sub_permutations)):
        sub_permutation = sub_permutations.pop()
        if not permutation_graph.get(sub_permutation):
            next_sub_permutations = generate_sub_permutations(sub_permutation)
            permutation_graph[sub_permutation] = next_sub_permutations
            for next_sub_permutation in next_sub_permutations:
                if not permutation_graph.get(next_sub_permutation):
                    sub_permutations.append(next_sub_permutation)
    return permutation_graph

def min_operations(arr):
    '''
    arr is an array of integers of 1 to N, 1 < N < 8
    '''
    pass

result = generate_permutation_graph('1234')
print(len(result))
for k in result:
    print(f'{k} : {result[k]}')