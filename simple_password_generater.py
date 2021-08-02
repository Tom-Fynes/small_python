from string import ascii_lowercase, ascii_uppercase, punctuation
from random import sample


def generate(length: int):

    contents = f"{ascii_lowercase}{ascii_uppercase}{punctuation}"
    password = "".join(sample(contents, length))
    return password

length = int(input("password length: "))

print(generate(length))
