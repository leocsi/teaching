import datetime# import a set of code from a library not originally included in the workspace
# for more on datetime: https://www.w3schools.com/python/python_datetime.asp
from random import randrange  # get a random number from 0-n
##################################
# Communication with the console #
##################################

print("Hello World!")  # print something to the console
print("------------")

user_input = input("Give some input: ")  # request input from the console (always store!!)
print("------------")

######################
# Types of variables #
######################

string = "this is a text"  # called a string - stores a sequence of characters
integer = 69  # called int - stores a natural number
float_numb = 0.3244  # called float - floating point number
boolean = False  # called boolean - True or False value
immutable_list = (1, 2, 3, 4)  # called a tuple - contains several values/variables
mutable_list = [1, 2, 3, 4]  # called a list - same, but can be changed
dictionary = {"a": 1,
              "b": 2,
              "c": 3
              }  # contains key value pairs (will be discussed later)

# always name your variables according to what they are storing!!!!!!

# good resource on variables : https://www.tutorialspoint.com/python/python_variable_types.htm

###############################
# Crucial variable operations #
###############################

print(integer + integer)  # addition of 2 int variables together(works with all the basic numeric operations)
print("------------")
print(string + string)  # concatenation of 2 strings
print("------------")

hour = datetime.datetime.now().strftime("%H")
minute = datetime.datetime.now().strftime("%M")
time = "{} h {}m".format(hour, minute)  # insert variables into the brackets
print(time)
print("------------")

mutable_list.append(4)  # puts a new element at the end of the list
mutable_list.remove(3)  # removes all occurrences of the given element
mutable_list.sort()  # sorts the list ( optional argument: reverse = True --> descending order)
print(mutable_list[0])  # first element of the list (labelled from 0!!)
print("------------")

print(mutable_list[randrange(len(mutable_list))])  # get a random element in the list(n is the size of the list here)


######################
# The if-else clause #
######################

if integer < float_numb:
    print("{} is smaller than {}".format(integer, float_numb))
elif integer == float_numb:
    print("Equal")
else:
    print("{} is larger than {}".format(integer, float_numb))
