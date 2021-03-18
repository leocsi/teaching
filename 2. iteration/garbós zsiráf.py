import string
from random import randrange

lowercase_letters = string.ascii_lowercase
uppercase_letters = string.ascii_uppercase
digits = string.digits

password = ""

for i in range(12):
    switch = randrange(3)
    if switch == 0:
        password += lowercase_letters[randrange(len(lowercase_letters))]
    elif switch == 1:
        password += uppercase_letters[randrange(len(uppercase_letters))]
    else:
        password += digits[randrange(len(digits))]
print(password)

