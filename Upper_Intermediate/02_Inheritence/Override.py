class Animal:

    def eat(self):
        print("This animal is eating")

class Rabbit(Animal):
    
    #overwitten
    def eat(self):
        print("This rabbit is earting a carrot")

rabbit = Rabbit()
rabbit.eat()