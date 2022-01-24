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
start_number = int(input(
    "Enter a start number"))  # made variable which represents the starting number, user will enter a starting number in the console
end_number = int(input(
    "Enter an end number"))  # made variable which represents the ending number, user will enter a starting number in the console
phrase = input("Enter any word")  # first phrase
phrase_2 = input("Enter another word")  # second phrase
phrase_3 = input("Enter another word")  # thrid phrase
for i in range(start_number, end_number):
    if i % 3 == 0 and i % 5 == 0:  # checks if number is divisible by 3 and 5
        print(phrase)
    elif i % 3 == 0:  # checks if number is divisible by 3
        print(phrase_2)
    elif i % 5 == 0:  # checks if number is divisible by 5
        print(phrase_3)
    elif i % 2 == 0:  # checks if number is even
        print("Even")
    else:
        print(i)

### if the player wanted to enter their own number they can follwo the steps bellow

# int(input("Enter a number between 1-100"))

# player_number = input("Enter a number")
# if int(player_number) % 3 == 0 and int(player_number) % 5 == 0:
#     print("Fizzbuzz")
# elif int(player_number) % 3 == 0:
#     print("fizz")
# elif int (player_number) % 5 == 0:
#     print("buzz")
