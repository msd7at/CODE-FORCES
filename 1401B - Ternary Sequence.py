t=int(input())
for q in range(t):
    x0,x1,x2=map(int,input().split())
    y0,y1,y2=map(int,input().split())
    m=min(x0,y2)
    y2-=m
    x0-=m
    m=min(x1,y0)
    x1-=m
    y0-=m
    m=min(x2,y1)
    x2-=m
    y1-=m
    s=2*m
    s=s-2*(min(x1,y2))
    print(s)
