# Abstract Class: 
# Prevent a User from crating an object of that class
# Compels the user to override abstract methods in a child class

# Abstract Class = a class which contains one or more abstract methods 
# Abstract method = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod

class Vihicle(ABC):
            # We need at least one method to avoid the user from creating object of the class

    @abstractmethod
    def go(self):
        pass
    @abstractmethod
    def stop(self):
        pass

class Car(Vihicle):
    def go(self):
        print("You drive the car")
    def stop(self):
        print("Your car has stopped")

class Motorcycle(Vihicle):
    def go(self):
        print("You ride the motorcycle")
    def stop(self):
        print("Your motorcycle has stopped")

#vihicle = Vihicle() # Does not instantiat because the class is Abstract
car = Car()
motorcycle = Motorcycle()

car.go()
motorcycle.go()