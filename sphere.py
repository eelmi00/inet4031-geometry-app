# inspiration code for Python Unit Testing Project

import math

def surfaceArea(r):
    # Surface area of a sphere = 4πr²
    return 4 * math.pi * (r ** 2)

def volume(r):
    # Volume of a sphere = (4/3)πr³
    return (4/3) * math.pi * (r ** 3)

def prompt():
    print()
    print("------------------------------------------------------------")
    print("PYTHON PROGRAM TO FIND THE VOLUME OF A SPHERE")
    print("------------------------------------------------------------")
    radius = int(input("Please Enter the radius : "))
    vol = volume(radius)
    print(f"The volume of a sphere with radius {radius} is: {vol}")

if __name__ == '__main__':
    prompt()
