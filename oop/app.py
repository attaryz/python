class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi , I'm {self.name}")


john = Person("John Doe")
print(john.name)
john.talk()