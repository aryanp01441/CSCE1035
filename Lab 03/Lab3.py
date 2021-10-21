lemon_juice_cups = float(input('Enter amount of lemon juice (in cups) :\n'))
water_cups = float(input('Enter amount of water (in cups) :\n'))
agave_nectar_cups = float(input('Enter amount of agave nectar (in cups) :\n'))
amount_servings = int(input('How many servings does this make?'))

print('Lemonade ingredients - yields', amount_servings, "servings")
print(lemon_juice_cups, "cup (s) lemon juice")
print(water_cups, "cup (s) water")
print(agave_nectar_cups, "cup (s) agave necatr")

user_servings = float(input("How many servings would you like?\n"))
i = user_servings / amount_servings

print(lemon_juice_cups * i, "cup (s) lemon juice")
print(water_cups * i, "cup (s) water")
print(agave_nectar_cups * i, "cup (s) agave necatr")
print('Lemonade ingredients - yields', amount_servings, "servings")
print((lemon_juice_cups * i) / 16, "gallon (s) lemon juice")
print((water_cups * i) / 16, "gallon (s) water")
print((agave_nectar_cups * i) / 16, "gallon (s) agave necatr")
