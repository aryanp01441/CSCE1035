# Define your function here
def miles_to_laps(user_miles):
    laps = user_miles / 0.25
    return laps

if __name__ == '__main__':
    # Type your code here. Your code must call the function. 
    values1 = float(input())
    output = miles_to_laps(values1)
    print('{:.2f}'.format(output))