class Car: 

    color = None

class Motorcycle:
    color = None

def changeColor(vehicle, color):
    vehicle.color = color

car_1 = Car()
car_2 = Car()
car_3 = Car()

motor_1 = Motorcycle()
motor_2 = Motorcycle()
motor_3 = Motorcycle()

changeColor(car_1, "red")
changeColor(car_2, "white")
changeColor(car_3, "blue")

changeColor(motor_1, "green")
changeColor(motor_2, "Purple")
changeColor(motor_3, "black")

print(car_1.color)
print(car_2.color)
print(car_3.color)

print(motor_1.color)
print(motor_2.color)
print(motor_3.color)