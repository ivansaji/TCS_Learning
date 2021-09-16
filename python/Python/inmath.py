import math

def Integer_Math(Side, Radius):
    # Write your code here
    s=int(Side)
    r=float(Radius)
    pi=3.14
    
    print("Area of Square is "+str(s**2))
    print("Volume of Cube is "+str(s**3))
    
    print("Area of Circle is "+str(round(pi*r**2,2)))
    print("Volume of Sphere is "+str(round(4/3*pi*r**3,2)))