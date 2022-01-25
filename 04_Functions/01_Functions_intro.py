# def woof(number_of_woofs):
#     for i in range(number_of_woofs):
#         print("WOOF!")
#     print("woof!")
#
#
# woof(17)
# def greeting(name):
#     print(f"Hello to you, {name}")

def double_plus_num(num1, num2):
    ans = (num1 * 2) + num2
    return ans
#  rule is all default arguments have to come after your default arguments

#when you don't know how many arguments you made input
# with multi arguments = multiargs

# def shopping (*items):  # * can allows you to put in multiargs
#     for item in items:
#         print(f"Dont forget to but an {item}")
# shout lets us know the multiarg has ended
#shopping("banana", "apple", "orange", shout = True)

# for default arguments and multiargs in one function
# def shopping (name, *items, shout = False):
#     if shout:
#         name = name.upper()
#     for item in items:
#         print(f"\{name}! Dont fotget to buy a {item}")
# shopping("David, banans, pele, shout = True")

#Type hints
def greeting(name: str):
    print(f"Hello to you, " + name)


def double_plus_num(num1: int, num2: int) -> int:
    ans = (num1 *2) + num2
    return ans

x = double_plus_num()

# functions should have clear names

def add_user():
    """
    Create a new user
    Promt for name and e-mail address
    store in databse
    """
    pass
# prevents errors
