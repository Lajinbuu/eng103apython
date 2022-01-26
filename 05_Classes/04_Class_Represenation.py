# class Location:
#     def __init__ (self, latitude, longitude):
#         self.latitude = latitude
#         self.longtitude = longitude
#
#     def __repr__(self):
#         return f" Location (latitude = {self.latitude}, longitude = {self.latitude})
#
#     def  __str__ (self):
#         return f"{self.latitude}, {self.latitude}"
#
#
#
class Dog:
    def __init__(self, age):
        self.age = age

    def __repr__(self):
        return f"Dog (age ={ self.age}"

    def __str__ (self):
        return f" A {self.age}+ Dgog"







# reper should give us representation
# def __str__ if a string is not provided then _rep_ will be used