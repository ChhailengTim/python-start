class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hello Mr. {self.name}")


test = Person("John Dara")
test.talk()

bob = Person("Bob Smith")
bob.talk()
