user_list = []

while True:
    user_input = int(input())

    if user_input < 0:
        break

    user_list.append(user_input)
  
print(min(user_list), "and", max(user_list))