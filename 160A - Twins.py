n=int(input())
l=list(map(int,input().split()))
s=sum(l)
c=0
ss=0
j=1
l.sort()
i=len(l)-1
while i>=0:
    ss+=l[i]
    s-=l[i]
    i-=1
    c+=1
    if ss>s:
        print(c)
        j=0
        break
    
if j:
    print(c)
