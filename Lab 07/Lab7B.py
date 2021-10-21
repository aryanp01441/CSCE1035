import math

list = []

def user_defined_list():
    list_range = int(input('Enter number of integers in list: '))
    j = 1
    while len(list) < list_range:
        user_num = int(input('Enter item #{}: '.format(j)))
        list.append(user_num)
        j += 1
    return list

def second_largest_number():
    list2 = list.copy()
    list2.sort()
    print('Second largest positive integer in list is', list[-2])

def positive_list():
    i = 0
    while i < len(list):
        if list[i] < 0:
            list[i] = abs(list[i])
        i += 1
    print('My now positive list is', list)

print('My original list:', user_defined_list())
print(list)
second_largest_number()
positive_list()
