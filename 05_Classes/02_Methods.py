# class Car:
#     def __init__(self, current_speed, increase = 0):
#         self.max_speed = 200
#         self.speed = self.accelerate(speed_change)
#         self.current_speed = current_speed
#
#
#     # dunder init method, set a max_speed attribute (and a current speed)
#     # implement the following methods:
#
#     # accelerate
#     # brake
#
#     def accelerate(self, speed_change):
#         speed = self.speed
#         max_speed = self.max_speed
#         if speed > max_speed:
#             print("Maximum speed")
#         elif speed < max_speed:
#
#
#         else:
#
#         self.speed_increase = # current speed - previous speed
#         # add the increase on to the current speed
#         pass
#     def break (self, speed_decrease):
#

# what happens if you accelerate beyond the max speed
# what happens if you brake past 0 mph

class Car:
    def __init__(self, max_speed ):
        self.max_speed = max_speed
        self._speed = 0

    # dunder init method, set a max_speed attribute (and a current speed)
    # implement the following methods:

    # accelerate
    # brake

    def accelerate(self, speed_increase):
        # if self.speed + speed_increase > self.max_speed:
        # self.speed = self.max_speed
        # else: self.speed += speed_increase
        #
        # self.speed += speed_increase
        self._speed = min(self.max_speed, self._speed + speed_increase)


    def brake (self, speed_decrease):
        if self._speed - speed_decrease < 0:
            self._speed = 0
        else:
            self._speed -= speed_decrease

    def get_speed(self):  # can gets speed officially for the user
        return self._speed





# _ hide variables, protects it
#__ makes the variable impenetable
car = Car(100)
print(car.max_speed)



# 4 pilas or OOP
