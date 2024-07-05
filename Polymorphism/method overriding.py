#Method Overriding
class Car:
    def gear(self):
        print("I have four gear")
class Sport_car(Car):
    def gear(self):
        print("I have seven gear")

obj=Sport_car()
obj.gear()

