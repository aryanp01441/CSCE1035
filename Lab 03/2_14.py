''' Women: Calories = ((Age x 0.074) - (Weight x 0.05741) + (Heart Rate x 0.4472) - 20.4022) x Time / 4.184 '''
''' Men: Calories = ((Age x 0.2017) + (Weight x 0.09036) + (Heart Rate x 0.6309) - 55.0969) x Time / 4.184 '''

''' Type your code here. '''
Age = int(input())
Weight = int(input())
Heart_Rate = int(input())
Time = int(input())

Women_calories = ((Age * 0.074) - (Weight * 0.05741) + (Heart_Rate * 0.4472) - 20.4022) * Time / 4.184
Men_calories = ((Age * 0.2017) + (Weight * 0.09036) + (Heart_Rate * 0.6309) - 55.0969) * Time / 4.184

print('Women: {:.2f} calories'.format(Women_calories))
print("Men: {:.2f} calories".format(Men_calories))