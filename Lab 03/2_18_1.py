lemon_juice_cups = float(input('Enter amount of lemon juice (in cups):\n'))
water_cups = float(input('Enter amount of water (in cups):\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups):\n'))
amount_servings = float(input('How many servings does this make?\n'))
print()

print('Lemonade ingredients - yields','{:.2f}'.format(amount_servings), 'servings')
print('{:.2f}'.format(lemon_juice_cups), "cup(s) lemon juice")
print('{:.2f}'.format(water_cups), "cup(s) water")
print('{:.2f}'.format(agave_nectar_cups), "cup(s) agave nectar\n")

user_servings = float(input("How many servings would you like to make?\n"))
print()
i = user_servings / amount_servings

print('Lemonade ingredients - yields','{:.2f}'.format(user_servings), 'servings')
print('{:.2f}'.format(lemon_juice_cups * i), "cup(s) lemon juice")
print('{:.2f}'.format(water_cups * i), "cup(s) water")
print('{:.2f}'.format(agave_nectar_cups * i), "cup(s) agave nectar")
print()

print('Lemonade ingredients - yields','{:.2f}'.format(user_servings), 'servings')
print('{:.2f}'.format((lemon_juice_cups * i) / 16), "gallon(s) lemon juice")
print('{:.2f}'.format((water_cups * i) / 16), "gallon(s) water")
print('{:.2f}'.format((agave_nectar_cups * i) / 16), "gallon(s) agave nectar")