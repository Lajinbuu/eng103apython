print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for num in x:
    if num % 2 == 0:
        print(num)

print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for num in x[:5]:
    if num % 2 == 0:
        print(num)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
initials = []
for i in names:
    print(i[0][-1])

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
# names.index("")
substring = []

for i in names:
    i.index(" ")
    my_string_index = i.index(" ")
    substring.append(my_string_index)
print(substring)

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:
list_of_initials = []
for i in names:
    initials = i[0] + i[-1]
    list_of_initials.append(initials)
print(list_of_initials)


# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]
# A3a:

list_without_duplicates = []

for i in list_of_lists:
    if len(i) == len(set(i)):
        list_without_duplicates.append(i)
print(list_without_duplicates)


# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:

# 1 create a while loop
# 2 within the loop there should be a variable which takes users input.
# there should be a line which compares the users input to 100
# if the user input is less than 100
# the user should be prompted to enter another number
# the user should be continuously prompted until the user enters a number greater than 100
# the loop should end once the user enters a number greater 100










user_number = 101

while user_number > 100:
    user_number = int(input("Please enter a digit greater than 100\n "))
    if user_number >= 100:
        print(user_number)
    else:
        print("Enter another digit")







print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:
