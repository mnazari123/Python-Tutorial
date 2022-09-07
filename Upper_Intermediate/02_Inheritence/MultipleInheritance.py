# Multiple Inheretance = when a child class is derived from more than one parent class

class Prey:
    def flee(self):
        print("This animal flees")

class Predator:
    def hunt (self):
        print("This animal is hunting")

class Fish(Prey, Predator):
    pass

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

hawk = Hawk()
rabbit = Rabbit()
fish = Fish()

hawk.hunt()
rabbit.flee()
fish.flee()
fish.hunt()
