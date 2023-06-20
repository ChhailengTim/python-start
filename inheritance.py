class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def talk(self):
        print("Woah Woah")


class Cat(Mammal):
    pass


dog = Dog()
dog.walk()

dog1 = Dog()
dog1.talk()