class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        print("person")
        return self.name == other.name


class Auto:

    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        print("auto")
        return self.name == other.name


jack1 = Person('Jack', 23)
jack2 = Person('Jack', 30)
print(jack1 == jack2)
print(jack1 is jack2)
a1 = Auto("Jack")
print(jack1 == a1)
print(a1 == jack1)
print(jack1 == "Jack")
