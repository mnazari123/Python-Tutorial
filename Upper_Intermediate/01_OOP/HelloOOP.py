from car import Car

car_1 = Car("Chevy", "Corvette", "2021", "Blue")
car_2 = Car("Ford", "Mustang", 2022, "red")


print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.wheels = 2 # one way to change the default value
# Car.wheels = 2 # change the value throughout the class. 

car_1.drive()
car_1.stop()
car_2.drive()
car_2.stop()


