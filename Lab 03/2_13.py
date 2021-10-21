''' Type your code here. '''
miles_gallon = float(input())
dollar_gallon = float(input())

value1 = (20 * dollar_gallon)/miles_gallon
value2 = (75 * dollar_gallon)/miles_gallon
value3 = (500 * dollar_gallon)/miles_gallon

print('{:.2f} {:.2f} {:.2f}'.format(value1, value2, value3))