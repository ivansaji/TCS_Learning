x=int(input())

ans = 0
if x==0 or x==1:
    ans=0

if x%2==0:
    ans=x-3
else:
    ans=x-1
    
print(ans)