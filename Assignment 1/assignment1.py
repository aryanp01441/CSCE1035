B1 = float(input("Please enter B1 in inches: "))
B2 = float(input("Please enter B2 in inches: "))
height = float(input("Please enter the height in inches: "))

area = (1/2) * (B1 + B2) * (height)

area_in_centimeters = 6.4516 * (area)

print("A trapezoid with B1 =", B1, "in. B2 =", B2, "in. and height =", height, "in. has an area of", area, "square inches or", area_in_centimeters, "square centimeters.\n")