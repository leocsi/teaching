import datetime

# Methods are pieces of code that are executed upon calling

##################################
# void method with no arguments #
##################################


def greet_user():  # the return type is called "void" because it does not return any values.
    hour = int(datetime.datetime.now().strftime("%H"))

    if hour < 12:
        part = "morning"
    else:
        part = "afternoon"

    print("good", part)

##################################
# void method with arguments #
##################################


def fibonacci(n):  # void function with an argument 'n' that prints the first n fibonacci numbers
    a_0 = 0
    a_1 = 1
    for i in range(n):
        temp = a_1
        a_1 = a_1 + a_0
        a_0 = temp
        print(a_1)


def print_nth_element(indexable, n):  # 2 arguments, 'n' being the specified element we need
    print(indexable[n])               # and indexable the variable that we are searching

# you can specify as many arguments as you need, but you have to provide all of them when calling the method

###################################
# return method with no arguments #
###################################


def request_file_path():
    path = input("Where is the file located?\nSpecify path: ")
    return path

################################
# return method with arguments #
################################


def exponential(number, power):
    product = number ** power
    return product

# note: it is possible to have a method return several values, then the returned variable will be a list

######################################
# calling the aforementioned methods #
######################################

# note: you cannot call a method before it is declared, ie: you cant call fibonacci before line 32


greet_user()  # <-- calling a method

fibonacci(5)                                       # be careful with your types, make sure that the method
print_nth_element(["a", "k", "w", "l", "dzs"], 3)  # receives the right kind of arguments when called

file_path = request_file_path()  # you usually want to store the return value, or use it instantly
print("The desired file is at: {}".format(file_path))

result = exponential(2, 10)  # 2 to the power of 10
print(result)
