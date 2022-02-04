import string
from random import randrange


lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits

password_length = 12

uppercase = 4
lowercase = 4
digit = 4

chars = ""

for i in range(lowercase):
    chars += lowercase_letters[randrange(len(lowercase_letters))]

for i in range(uppercase):
    chars += uppercase_letters[randrange(len(uppercase_letters))]

for i in range(digit):
    chars += digits[randrange(len(digits))]


table = []

for i in range(len(chars)):
    table.append(i)

print(table)

final_password = "************"

for i,v in enumerate(chars):
    rand = randrange(len(table))
    element = table[rand]
    table.remove(element)
    final_password = final_password[:element] + v + final_password[element+1:]
