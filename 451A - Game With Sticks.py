
n,m=map(int,input().split())
c=0
while n and m:
    n-=1
    m-=1
    c+=1
if c%2:
    print("Akshat")
else:
    print("Malvika")
