print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
# def name (int)
# range (1, n)
# between a range with 1 being the lowest value and n being the highest
# the numbers within that range should return % ==0, the numbers which return %==0 should be listed
# t = []
# i want to take the numbers in the range which can be divided by the number inputed
# i then want to return the numbers produced and put them into a list
#attempt 1
# def divisors (num):
#     for integer in range(1, num):
#         if integer % integer == 0:
#
#     return integer
#
# attempt 2
def divisors(n):
    empty_list = []
    for i in range(1, int(n+ 1)):
        if n % i == 0:
            empty_list.append(i)
    print(empty_list)


divisors(8)


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:
def factorials (num1, num2):
    if num1 % num2 == 0:
        print(num1)
    elif num2 % num1 == 0:
        print(num2)
factorials(3,9)



# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet
# alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
#             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

# A2a:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
             "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
# def number_assigner (string):
# my_list = []
#     for i in string.index([]):
#         print(string)
# number_assigner(alphabet)


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:



print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:



# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:



print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:



# -------------------------------------------------------------------------------------- #