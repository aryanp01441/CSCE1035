# Define your function here.
def integer_to_reverse_binary(num1):
    res = ""
    while (num1 > 0):
        res += str(num1%2)
        num1 = num1 // 2
    return res

def reverse_string(inputString):
    res = ""
    for x in inputString:
        res=x+res
    return res
    
    
if __name__ == '__main__':
    # Type your code here. Your code must call the function.
    n = int(input())
    print(reverse_string(integer_to_reverse_binary(n)))