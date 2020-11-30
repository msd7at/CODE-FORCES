s1=input()
s2=input()
ss=1
for i in range(len(s1)):
    a=s1[i].lower()
    b=s2[i].lower()
    if a==b:
        pass
    elif  a<b:
        print(-1)
        ss=0
        break
    else:
        print(1)
        ss=0
        break
    
if ss:
    print(0)
