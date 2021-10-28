''' Type your code here. '''
user_num = int(input())

i = 1
max = 0

while i > 0:
    i = user_num
    user_num = int(input())
    if max < user_num:
        max = user_num

print(max)