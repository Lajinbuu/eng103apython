# dictionaries

# key- value pairs

my_dict = {"key": "value"}

table = {
    "name": "The table",
    "colour": "light brown",
    "dimensions" : {
        "height": 120,
        "length": 200,
         "width": 150
    }
}

print(table.get("dimensions").get("width"))
print(table["dimensions"]["width"])
print(table.keys()) # returns the keys
print(table.values()) # returns the content of keys
print(table.items()) # shows keys and content as a tuples











# print(table["colour"])### to enter an item in a dictionary, dictionary name then dictionary [key]
#
# table["height"] = 125
# table ["price"] = 99.99
# print(table)
#
# table.update({"price": 99.99, "height": 125})
# print(table.get("price"))
#
# print(table.get("price"))
# print(table["price"])
## difference is 'get looks for price, finds it and prints it
## square brackets looks for the key price and then prints it
