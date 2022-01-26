# Basic version
# for numbers 1 to 100
# play fizzbuzz
# print the number
# if the divisible by 3 fizz
# if divisible by 5 buzz
# if both fizzbuzz


# what can you add?
# can we customise the end number
# or the start number#
# can we get those from player input
# can we input alternate words for fizz and buzz?

# for i in range(1,101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("Fizzbuzz")
#     elif i % 3 == 0:
#         print("fizz")
#     elif i % 5 == 0:
#         print("buzz")
#     elif i % 2 == 0:
#         print("Even")


# number = numbers[0:101], but have to inout
# start_number = int(input("Enter a start number"))  # made variable which represents the starting number, user will enter a starting number in the console
# end_number = int(input("Enter an end number"))  # made variable which represents the ending number, user will enter a starting number in the console
# phrase_1 = input("Enter any word")  # first phrase
# phrase_2 = input("Enter another word")  # second phrase
# phrase_3 = input("Enter another word")  # thrid phrase
# users_number = input("Enter a valid number")
# should allow the user to enter a name for fizz and a name for buzz
# takes two numeric inputs from the user.
# sees if the range of numbers between the inputs are factors of 15 or are factors of both 3 and 5
# if the number in the range is a factor of 15 say fizzbuzz
# if the number in the range is a factor of 5 say buzz
# if the number in the range is a factor of 3 say fizz
#
#
#
#
def user_input():
    start = int(input("Please enter your first number: "))
    end = int(input("Please enter your second number: "))
    fizzbuzz = input("Please enter a word to replace fizzbuzz: ")
    buzz = input("Please enter a word to replace buzz: ")
    fizz = input("Please enter a word to replace fizz: ")
    return start, end, fizzbuzz, buzz, fizz


def fizzbuzz_operator(start, end, fizzbuzz, buzz, fizz):
    for num in range(start,end):
        if num % 15 == 0:
            print(fizzbuzz)
        elif num % 5 == 0:
            print(buzz)
        elif num % 3 ==0:
            print(fizz)
        else:
            print(num)



# get the user input from the user input function
# and pass the user input in the fizzbuzz_operator
start_in, end_in, fizzbuzz_in, buzz_in, fizz_in = user_input()
fizzbuzz_operator(start_in, end_in, fizzbuzz_in, buzz_in, fizz_in)

    # if numbers in range(start,end) 15 % == 0
    # print(fizzbuzz)
    #elif numbers in range (start,end) 5 % == 0
    #print(buzz)
    #elif numbers in range (start,end) 3 % ==0
    # print(fizz)
    # else user should try again





#  older code
# users_number = input("Enter a digit")
# if users_number.isdigit():
#     for i in range(start_number, end_number):
#         if i % 3 == 0 and i % 5 == 0:  # checks if number is divisible by 3 and 5
#             print(phrase)
#         elif i % 3 == 0:  # checks if number is divisible by 3
#             print(phrase_2)
#         elif i % 5 == 0:  # checks if number is divisible by 5
#             print(phrase_3)
#         else:
#             print(i)
#
#
# older code

# dry = don't repeat yourself
### if the player wanted to enter their own number they can follow the steps bellow

# int(input("Enter a number between 1-100"))

# player_number = input("Enter a number")
# if int(player_number) % 3 == 0 and int(player_number) % 5 == 0:
#     print("Fizzbuzz")
# elif int(player_number) % 3 == 0:
#     print("fizz")
# elif int (player_number) % 5 == 0:
#     print("buzz")
