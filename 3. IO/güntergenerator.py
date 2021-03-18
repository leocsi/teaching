from random import randrange

with open("C:\Code\Teaching\\3. IO\german_names.txt", 'r') as file:
    data = file.readlines()
    file.close()

ui = input("What do you identify with?").strip()

if ui == "man":

    limit = 68
elif ui == "woman":
    limit = len(data)
else:
    limit = len(data)

print(data[randrange(limit)])



