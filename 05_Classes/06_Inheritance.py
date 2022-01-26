# Inheritance ane Polymorphism
# need to think what's already in the super class
# then whatever I want to do in the sub class
# I can customise
#
class Mammal:
    def __int__ (self, name):
        self.warm_blooded = True
        self.name = name

    def reproduce(self):   # method
        print("Giving birth to live young")


class Platypus(Mammal):
    def __init__(self, name):
        super.__init__(name)
        self.poisonous_bars = True
    def reproduce(self):
        print("Laying eggs")
# the newsest variable you change bbecomes the latest
class Horse(Mammal):       # putting Mammal in brackets starts the inheritance
    def __init__(self, name, jockey):      # initilation method here can change the parent
        super().__init__(name)     # calls on the parent class
        self.legg = 4
        self.jokcey = jockey

    def pregnancy(self):
        print("wait 11 months...")
        super().reproduce()

# example of method overloading
# in other languages you can create methods with the name anme
# you can then change the parementers of the method to your desire
# in python you need to set the method to except a paramter and then
# say in the method =1, so python knows than one input
# in its method pararmeter
class Pony(Horse):
    def __init__ (self, pony_name, cuteness_rating=10):
        super(). __init__(pony_name, None)

    def give_birth(self, number_of_offspring =1):
        for i in range(number_of_offspring):
            super().reproduce()
# the order in which you change a method decides what method will be take first


p = Pony("Twinkle Toes")
print(p.legs)
p.give_birth
