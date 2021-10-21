def is_list_even(my_list):
        for i in range(len(my_list)):
            if my_list[i] % 2 != 0:
                return False
        return True
        
def is_list_odd(my_list):
        for i in range(len(my_list)):
            if my_list[i] % 2 == 0:
                return False
        return True

if __name__ == '__main__':
    my_list = []
    n = int(input())
    for i in range(n):
        my_list.append(int(input()))
        
        
    if is_list_even(my_list):
        print('all even')
    elif is_list_odd(my_list):
        print('all odd')
    else:
        print('not even or odd')