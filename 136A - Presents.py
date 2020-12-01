n=int(input())
l=list(map(int,input().split()))
ans=[0]*n
for i in range(n):
    v=i+1
    ans[l[i]-1]=v
print(*ans,end=" ")
