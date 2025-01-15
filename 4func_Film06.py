import math

sphere_radius = float(input("Input radius "))
def sphere_volume(r):
    volume = ((4/3)*(math.pi * r ** 3))
    return volume

print(f'{sphere_volume(sphere_radius):.2f}')
