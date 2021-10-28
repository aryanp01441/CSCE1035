''' Type your code here. '''
list = []

user_input = input()
i = 1

while user_input != '*':
    list.append(user_input)
    user_input = input()

length = len(list) + 1
while i < length:
    print(list[-i] + ",", end='')
    i += 1
print()