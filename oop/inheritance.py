class Animal:
    def walk(self):
        print('walk')

# classes Dog and Cat inherits walk function from its parent class Animal
# Dog and Cat classes can have it's own functions    
class Dog(Animal):
    def bark(self):
        print('bark')


class Cat(Animal):
    def meow(self):
        print('meow')


dog1 = Dog()
dog1.walk()


cat1 = Cat()
cat1.meow()


class Bird(Animal):
# pass keyword tells python to skip this line
# you cannot leave a class empty
    pass