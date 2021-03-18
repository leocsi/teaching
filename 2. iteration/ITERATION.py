def section(s):
    print("\n"+"_______________")
    print("------"+str(s)+".------"+"\n")


def dist(n):
    print("\n"+"______"+str(n)+".______"+"\n")

###############################
# I. given number of repeats: #
###############################


for i in range(3):  # from 0-2
    print(i)

dist(2)  # --dont mind these
for i in range(10, 15):  # from 10-14
    print(i)

dist(3)
for i in range(3, 12, 3):  # from 3-12, by leaps of 3
    print(i)

dist(4)
array = ['a', 'b', 'c', 'd', 'e']

for i in array:  # loop through the elements of an array
    print(i)

dist(5)
for i in range(len(array)):  # alternative array iteration
    print(array[i])

dist(6)
for i, j in enumerate(array):  # i: counter, j: the element of the array we are iterating
    print("{}. element of array: {}".format(i, j))

section("II")
###################################
# II. uncertain amount of repeats #
###################################

condition = True  # can be a single variable
while condition:
    ui = input("Press X for quitting: ")
    if ui == "X":
        break
    # alternatively
    # if ui == "X":
    #     condition = False
dist(1)

a = 0
b = 0
while a + b <= 15:  # or it can be an expression
    print(a+b)
    a += 1
    b += 2
