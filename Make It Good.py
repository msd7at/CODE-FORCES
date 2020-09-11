t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    i=n-1
    while l[i]<=l[i-1] and i>0:
        i-=1
    while l[i]>=l[i-1] and i>0:
        i-=1
    print(i)
    
