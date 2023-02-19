class Circle:

    def __init__(self, radius):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = float(value)

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, value):
        self.__radius = value / 2


circle = Circle(42)
print(circle.radius)
print(circle.diameter)
circle.diameter = 100
print(circle.radius)
print(circle.diameter)
