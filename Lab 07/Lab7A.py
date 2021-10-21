import math

def calc_hex_area(length):
    return 3 * math.sqrt(3) * length * length

def calc_side_area(length, base):
    return 6 * length * base

def display_surface_area(length, base):
    print('The total surface area is {:.3f} square feet'.format(calc_side_area(length, base) + calc_hex_area(length)))

prism_height = float(input('Enter height of hexagonal prism in feet: '))
prism_length = float(input('Enter length of the base edge in feet: '))

print('Surface area of hexagonal faces is {:.3f} square feet'.format(calc_hex_area(prism_length)))
print('Surface area of rectangular sides is {:.3f} square feet'.format(calc_side_area(prism_length, prism_height)))
display_surface_area(prism_length, prism_height)