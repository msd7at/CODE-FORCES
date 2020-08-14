t=int(input())
for q in range(t):
    l=list(map(int,input().split()))
    l.sort()
    if l[1]==l[2]:
        print('YES')
        print(l[2],l[0],l[0],end=" ")
        print()
    else:
        print("NO")
