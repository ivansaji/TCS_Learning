import math
#
# Complete the 'calc' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER c as parameter.
#

def calc(c):
    # Write your code here
    c=float(c)
    r = float(c/(2*math.pi))
    r=round(r,2)
    area = float(math.pi*(math.pow(r,3)))
    area=round(area,2)
    
    return r,area