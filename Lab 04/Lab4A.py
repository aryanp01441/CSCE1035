import random

def Convert(string) :
    list1 = []
    list1[:0] = string
    return list1

str1 = input('Enter a string (>1 character) to be incrypted: ')
list = Convert(str1)

num_random = random.randint(97, 122)
char_random = chr(num_random)
print('Original List:', list)

list2 = []
i = 2
list_len = len(list)

while i != list_len:
    list2.append(list[i])
    i += 1

list2.append(char_random)
list2.append(list[0])
list2.append(list[1])
print('Encrypted list:', list2)

def listToString(list2):
    str2 =''

    for ele in list2:
        str2 += ele
    return str2

print('Encrypted string:', listToString(list2))