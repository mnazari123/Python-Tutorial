# Duck Typing = concept where the class of an object is less important than the methods 
#               class type is not checked if minimum method/attribute are present
#               "if it walks like a duck, and quacks like a duck, then it must be a duck Typing"


class Duck:
    def walk(self):
        print("This duck is walking")
    def talk(self):
        print("This duck is quacking")

class Chicken: 
    def walk(self):
        print("This checken is walking")
    def talk(self):
        print("This chicken is clucking")

class Person: 
    def catch(self, something):
        something.walk()
        something.talk()
        print("You caught the critter!")

duck = Duck()
chicken = Chicken()
person = Person()

person.catch(duck)
person.catch(chicken)