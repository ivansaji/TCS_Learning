def generateList(startvalue, endvalue):
    # Write your code here
    a=[]
    for i in range(startvalue,startvalue+3):
        a.append(i)
    print(a)
    b=[]
    for i in range(endvalue,endvalue-5,-1):
        b.append(i)
    print(b)
    c=[]    
    for i in range(startvalue,endvalue,4):
        c.append(i)
    print(c)
    d=[]
    for i in range(endvalue,startvalue-1,-2):
        d.append(i)
    print(d)