
class Car:
    
    wheels = 4 # class variable 

    def __init__(self, make, model, year, color): # __init__ is the same as construtor in java
        self.make = make # instance Variable
        self.model = model # instance Variable 
        self.year = year # instance Variable
        self.color = color # instance Variable

    def drive(self):
        print("This "+self.model+" is drivin")
    
    def stop(self):
        print("This "+self.model+" is stopping")
