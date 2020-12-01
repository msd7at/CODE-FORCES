n=int(input())
s=[4,7,44,77,47,74,444,777,477,447,744,474,747,774]
t=0
for i in s:
    if n%i==0:
        print("YES")
        t=1
        break
if t==0:
    print("NO")
