import math
# Add any extra import statements you may need here

UPPERCASE_MIN = 65 # 'A'
UPPERCASE_MAX = 90 # 'Z'
LOWERCASE_MIN = 97 # 'a'
LOWERCASE_MAX = 122 # 'z'


# Add any helper functions you may need here
def rotate_alpha_char(char, rotation_factor):
    ascii_code = ord(char)
    is_uppercase = ascii_code <= UPPERCASE_MAX
    translated = ascii_code - UPPERCASE_MIN if is_uppercase else ascii_code - LOWERCASE_MIN
    
    rotated = (translated + rotation_factor) % 26
    return chr(rotated + UPPERCASE_MIN if is_uppercase else rotated + LOWERCASE_MIN)


def rotate_digit_char(char, rotation_factor):
    translated = int(char)  # we assume it is numeric
    return str((translated + rotation_factor) % 10)

def rotate_char(char, rotation_factor):
    if char == '-':
        return char
    if char.isalpha():
        return rotate_alpha_char(char, rotation_factor)
    if char.isnumeric():
        return rotate_digit_char(char, rotation_factor)
    return char

def rotationalCipher(input, rotation_factor):
  # Write your code here
    result = ''
    for char in input:
        result += rotate_char(char, rotation_factor)
    
    return result

def printString(string):
    print('[\"', string, '\"]', sep='', end='')


test_case_number = 1

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!
def check(expected, output):
    global test_case_number
    result = False
    if expected == output:
        result = True
    rightTick = '\u2713'
    wrongTick = '\u2717'
    if result:
        print(rightTick, 'Test #', test_case_number, sep='')
    else:
        print(wrongTick, 'Test #', test_case_number,
              ': Expected ', sep='', end='')
        printString(expected)
        print(' Your output: ', end='')
        printString(output)
        print()
    test_case_number += 1


if __name__ == "__main__":
    input_1 = "All-convoYs-9-be:Alert1."
    rotation_factor_1 = 4
    expected_1 = "Epp-gsrzsCw-3-fi:Epivx5."
    output_1 = rotationalCipher(input_1, rotation_factor_1)
    check(expected_1, output_1)

    input_2 = "abcdZXYzxy-999.@"
    rotation_factor_2 = 200
    expected_2 = "stuvRPQrpq-999.@"
    output_2 = rotationalCipher(input_2, rotation_factor_2)
    check(expected_2, output_2)

    # Add your own test cases here
