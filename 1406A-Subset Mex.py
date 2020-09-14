t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    N=[0]*101
    for i in l:
        N[i]+=1
    s=0
    for i in range(101):
        if N[i]>0:
            N[i]-=1
        else:
            s=i
            break
    for i in range(101):
        if N[i]>0:
            N[i]-=1
        else:
            s=s+i
            break
    print(s)
        
        
        
