a = "abc"
str = "a to {}".format(a)
print(str)
b = 4.2
c = 5
str2 = "{0} + {1} = {2}".format(b, c, b + c)
print(str2)
b = 4.2
c = 5
str2 = "{0:f} + {1:d} = {2:e}".format(b, c, b + c)
print(str2)
