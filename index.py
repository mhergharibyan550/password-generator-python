from tools import generate_password


password_length = int(input("Input password length: "))
password = generate_password(password_length)

print(password)
