from random import randint


def generate_password():
    password_length = int(input("Input password length: "))
    assert isinstance(password_length, int), "Password should be a valid number"

    password_char_list = []

    for i in range(password_length):
        ascii_decimal_char = randint(0, 127)
        password_char_list.append(chr(ascii_decimal_char))

    return str(password_char_list)
