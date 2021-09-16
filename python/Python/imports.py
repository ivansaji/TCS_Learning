import math

def calc(c):
    # Write your code here
    c=float(c)
    r = float(c/(2*math.pi))
    
    area = float(math.pi*(math.pow(r,2)))
    r=round(r,2)
    area=round(area,2)
    
    return r,area
