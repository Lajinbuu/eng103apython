# i = 1
# keep_looping = True
# while i < 10:
#     print(i)
#     if i == 5:
#         print("Five Party")
#         break ## will break the nearest loop, in this case breaks after "five party"
#     i += 1
#     print("Start again")
#
#     setting condition to false will not instantly break the loop, unlike break
#
#
#     # break ends loop as soon as we hit it
    # += 1 #incriment by one each time
# for x in range["a", "b", "c"]:
#     break_for = False
#     i = 100
#     while i < 110:
#         print(x, 1)
#         if x == "b" and i == 105:

# age = int(input("What is your age? \n"))
# age = None also works
# prompt_user = True
# while prompt_user:
#     age = input("What is your age? \n")
#     if age.isdigit():
#         prompt_user = False
#     else:
#         print("PLease enter age in digits")
#
# print(f"Double your age is {int(age) * 2}")

age = None
prompt_user = True
while prompt_user:
        age = input("What is your age? \n")
        if age.isdigit():
            if int(age) <= 119:
                prompt_user = False
        else:
            print("PLease enter age in digits")





