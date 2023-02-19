class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


jack1 = Person('Jack', 23)
jack2 = Person('Jack', 23)
print(jack1 == jack2)
print(jack1 is jack2)
