import math
''' Type your code here. '''
x = float(input())
y = float(input())
z = float(input())

value_1 = x ** z
value_2 = x ** (y ** z)
value_3 = abs(x-y)
value_4 = math.sqrt(x ** z)

print("{:.2f} {:.2f} {:.2f} {:.2f}".format(value_1, value_2, value_3, value_4))