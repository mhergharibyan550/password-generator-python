from random import randint


def generate_password(password_length: int):
    assert isinstance(password_length, int), "Password should be a valid number"
    assert password_length > 5, "Password length must be at least 6 characters"

    password_char_list = []

    for i in range(password_length):
        isdigit = True if randint(0, 1) == 1 else False

        if isdigit:
            password_char_list.append(str(randint(0, 9)))
        else:
            ascii_decimal_char = randint(33, 126)
            password_char_list.append(chr(ascii_decimal_char))

    return "".join(password_char_list)
