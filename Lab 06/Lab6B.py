user_input = int(input('Size of multiplication table: '))
print('  x |  ', end=' ')

i = 1
j = 1
k = 0
x = 0
while i <= user_input:
    print(i, end='\t')
    i += 1
print()
print('----+', end='')
while x  <= user_input:
    print('----', end='')
    x += 1
print()
while j <= user_input:
    if j < 10:
        print(' ', j, '|', end='\t')
    else:
        print('', j, '|', end='\t')
    for k in range(1, user_input + 1):
        print(k * j, end='\t')
    print()
    j += 1