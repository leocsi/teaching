from random import randint

ui = int(input("Guess"))
number = randint(1, 10)

print(number)

while ui != number:
    if ui < number:
        ui = int(input("higher"))
    else:
        ui = int(input("lower"))


print("You got it")
