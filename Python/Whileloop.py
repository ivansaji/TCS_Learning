def calculateNTetrahedralNumber(startvalue, endvalue):
    a=[]
    # Write your code here
    i=int(startvalue)
    while(i!=int(endvalue+1)):
        x=i*(i+1)*(i+2)
        x=x/6
        a.append(int(x))
        i+=1
    return a