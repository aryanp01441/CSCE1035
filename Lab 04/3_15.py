caffeine_mg = float(input())

''' Type your code here. '''
caffeine_mg1 = caffeine_mg / 2
caffeine_mg2 = caffeine_mg1 / 2
caffeine_mg3 = caffeine_mg2 / (2 ** 2)

print('After 6 hours:', end=' ')
print('{:.2f}'.format(caffeine_mg1), 'mg')
print('After 12 hours:', end=' ')
print('{:.2f}'.format(caffeine_mg2), 'mg')
print('After 24 hours:', end=' ')
print('{:.2f}'.format(caffeine_mg3), 'mg')