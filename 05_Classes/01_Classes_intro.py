# OPP - Object Orietned Programming
# classes use uppercases
class Dog:

    animal_king = "Canine" # varoiable

    def bark(self): # method
        return "WOOF!"
    def loud_bark(self):
        return self.bark().upper()

# self is very important in methods
# self exists soley in the a class, when you a defining
# can call functions already made in a class
#

fido = Dog()
print(fido, type(fido))
print(fido.animal_king)
print(fido.bark())


class Jaguar:
    species = "Feline"

    def growl(self):
        return "GROWL"
    def loud_growl(self):
        return self.growl().upper()


# instantiation i.e a module can be assigned ot multiple variables

fido = Dog()
lassie = Dog()

print(fido.animal_king)
dog.animal_king = "giraffe"
print()
