# Lists
shopping_list = ["eggs", "bread", "bananas", "tea"]
print(shopping_list, type(shopping_list))


print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list[2] = "milk"
# indesing has to be in the length of the existing list e.g
# shopping_list[4] = " biscuits" will not work

# # to add to a list
# shopping_list.append("biscuits")
# print(shopping_list)
# # reverse of append is remove
# shopping_list.remove("bread")
# shopping_list.append("bread")
# shopping_list.append("bread")
# shopping_list.remove("bread")
# shopping_list.pop(-1) # pop removes the thing you have removed it also show you what you have removed
# print(shopping_list)

# mixed lists
# mixed = [1, 2, "three", True, None, ["another", "lists"]]
# print(mixed)
# mixed[1] =2.0
#
# ## lists are mutable, can mutate, can change
# print(mixed[:4]) # will include everythin up to but not including 4
# print(mixed[5])

colours = ("red", "blue", "green" )
print(colours, type(colours))
#Tuples are IMMUTABLE
print(colours.count("red"))
print(colours.index("green"))

list_in_tuple = (
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
)
print(len(list_in_tuple))
print(list_in_tuple[0][-1])
## tuples are immutableee



## lists continues

text = "It was the best of times"
text_list = text.split(" ")

print(text_list, type (text_list))

csv = "12, 355, 3456, 456, 67, 78 "
csv_list = csv.split(",")
print(csv)

#join
test_star = "---".join(text_list)
print(" ".join(csv_list))

n = [56, 32, 56, 678, 23, 1, 8]
n.sort()
# will sort it
# sorted will change thi list
