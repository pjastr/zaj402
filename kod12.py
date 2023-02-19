class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def set_x(self, value):
        self.__x = value

    def set_y(self, value):
        self.__y = value


point = Point(12, 5)
print(point.get_x())
print(point.get_y())
point.set_x(42)
print(point.get_x())
# print(point.__x)
