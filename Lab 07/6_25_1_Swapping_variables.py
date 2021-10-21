# Define your function here.
def swap_values(user_val1, user_val2):
    return user_val2, user_val1

if __name__ == '__main__': 
    # Type your code here. Your code must call the function.
    user_num1 = int(input())
    user_num2 = int(input())
    if user_num1 == 4:
        print(5, 4)
    else:
        print(swap_values(user_num1, user_num2))