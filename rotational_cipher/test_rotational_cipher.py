from .rotational_cipher import rotate_alpha_char, rotate_digit_char, rotationalCipher

def test_rotate_alpha_char():
    # from example -- test with 3
    assert rotate_alpha_char('Z', 3) == 'C'
    assert rotate_alpha_char('F', 3) == 'I'
    assert rotate_alpha_char('z', 3) == 'c'
    assert rotate_alpha_char('a', 3) == 'd'
    assert rotate_alpha_char('f', 3) == 'i'
    assert rotate_alpha_char('A', 3) == 'D'

    # testing negative rotations
    assert rotate_alpha_char('A', -1) == 'Z'
    assert rotate_alpha_char('A', -26) == 'A'
    assert rotate_alpha_char('A', -27) == 'Z'
    assert rotate_alpha_char('a', -1) == 'z'
    assert rotate_alpha_char('a', -26) == 'a'
    assert rotate_alpha_char('a', -27) == 'z'

def test_rotate_digit_char():
    # from example -- test with 3
    assert rotate_digit_char('0', 3) == '3'
    assert rotate_digit_char('9', 3) == '2'
    assert rotate_digit_char('3', 3) == '6'

    # test full rotations
    assert rotate_digit_char('9', 10) == '9'
    assert rotate_digit_char('9', -10) == '9'

def test_cipher():
    assert rotationalCipher(
        'All-convoYs-9-be:Alert1.',
        4
    ) == 'Epp-gsrzsCw-3-fi:Epivx5.'

    assert rotationalCipher(
        'abcdZXYzxy-999.@',
        200,
    ) == 'stuvRPQrpq-999.@'