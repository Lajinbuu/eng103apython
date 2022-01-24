# i = 375 # int
# f = 3.75 # float
# c = 3j +2 # complex number
#
# print(c, type(c))
# add = 3+5
# subtract = 3-5
# multiply = 3 * 5
# divide = 3 / 5
# power = 3**5
# modula = 3 % 5
# print (13 // 3) # makes the number a whole number, to the lowest nunber
# # or
# print(14 // 3, 14 % 3)

# single = "string in single quotes"
# double = "string in double quotes"
# both = "this is Latif's \"string\""
#
#
# # indexing and slicing
# hi = "Hello World!"
# print(hi[6]) #w
# print(hi[0:6]) # includes first upto the assinged
# print(hi[3:8])
# print(len(hi))
#
# # methods
#
# white_space = "   lots of white space   "
# print(len(white_space))
# print(white_space.strip()) # no white spaces at either end now
# print(white_space.rstrip()) # strips from the left and not the right
# print(white_space.upper())## makes string upper case
# print(white_space.strip().capitalize()) # capitalise alone will not capitalise the variable but . strip first will
# print(white_space(" "))
# print(white_space.strip().count(" "))# will count the number of spaces
# print(white_space.replace"o", "ooooo".replace("i", "ooo"))
#
# print(white_space)
# ## f-strings (formatted strigns)
# pi= 3.14159265959
# print(f"Pi to 3dp:{pi:3f}")
#
# score = 16
# max_score =26
# print(f"you scored {score / max_score}")
# print(f"you scored {score / max_score: .2f}")# 2 decimal palces
# print(f"you scored {score / max_score:%}") # percentage
# print(f"you scored {score / max_score: .2%}")# percentage plus 2 decimal places

#boolean

# t = True
# f = False
# print(t, type(t))
# print(t, type(t))
#
# print(3+2 == 5)
# # print(5 != 5 )
# print (True and True)

# age = 19
# drink = "alcohol"
# print(age > 18 and drink == alcohol)

hi = " Hello World"
#print(hi.isalpha())
#print(hi.endswith())
#print(hi.startswith())
#print(hi. upper())
#print(hi.lower())

# print(hi.strip(" World").isalpha())
# print(hi.lower().islower())
# print(hi.upper().isupper())
# print(hi.endswith("ld"))
# print(hi.startswith(" H"))

print(bool(1))
print(bool(0))
print(bool(98))
print(bool(-1.5))
print(bool)
print(int(bool(False)))
print(int(bool(True)))

print(bool("Hello"))
empty = ""
print(empty, type (empty), bool(empty))
#none

n = None
print(n, type(n))
print(bool(None))
print(n is None) # is instead of ==, python prefers it
print(type(15) is int)


