num1 = float(input())
num2 = float(input())
num3 = float(input())
num4 = float(input())

''' Type your code here. '''
num_products = num1 * num2 * num3 * num4
num_average = (num1 + num2  + num3 + num4) / 4

print('{:.0f}'.format(num_products), '{:.0f}'.format(num_average))
print('{:.3f}'.format(num_products), '{:.3f}'.format(num_average))