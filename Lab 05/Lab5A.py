user_str = input('Type a message to encode: ')

user_str = user_str.upper()

user_str = user_str.replace(" ", "")

top = ""
bottom = ""

count = 0
for i in user_str:
    if count % 2 == 0:
        top += user_str[count]
    else:
        bottom += user_str[count]
    count = count + 1

cipher = top + bottom
print(cipher)