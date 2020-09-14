t=int(input())
for q in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    l.sort()
    x=l[0]*l[1]*l[n-3]*l[n-2]*l[n-1]
    y=l[0]*l[1]*l[2]*l[3]*l[n-1]
    z=l[n-3]*l[n-2]*l[n-1]*l[n-4]*l[n-5]
    print(max(x,y,z))
