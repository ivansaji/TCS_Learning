def find(num1, num2, num3):
    # Write your code here
    a=int(num1)
    b=int(num2)
    c=int(num3)
    
    if(a<b and b>=c):
        val1=True
    else:
        val1=False
    
    if(a>b and b<=c):
        val2=True
    else:
        val2=False
    
    if(a==c and a!=b):
        val3=True
    else:
        val3=False
        
    print(val1,val2,val3,sep=" ")