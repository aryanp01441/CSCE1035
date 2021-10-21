''' Type your code here. '''
f0 = int(input())

value_1 = f0
value_2 = f0*((2 ** (1/12))**1)
value_3 = f0*((2 ** (1/12))**2)
value_4 = f0*((2 ** (1/12))**3)
value_5 = f0*((2 ** (1/12))**4)

print("{:.2f} {:.2f} {:.2f} {:.2f} {:.2f}".format(value_1, value_2, value_3, value_4, value_5))