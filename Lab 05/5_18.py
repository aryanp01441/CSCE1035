def reversed_string(str):
    return str[::-1]

while True:
    s = input()
    if s == 'Done' or s == 'done' or s == 'd':
        break;
    else:
       print(reversed_string(s))