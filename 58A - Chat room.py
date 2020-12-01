#SOLUTION 1
s=input()
a="hello"
i=0
for j in s:
    if j==a[i]:
        i+=1
    if i==5:
        break
    
if i==5:
    print("YES")
else:
    print("NO")
    
    
    
#SOLUTION 2
s=input()
an=""
t=0
for i in s:
    if an=="" and i=="h":
        an+=i
    elif an=="h" and i=="e":
        an+=i
    elif an=="he" and i=="l":
        an+=i
    elif an=="hel" and i=="l":
        an+=i
    elif an=="hell" and i=="o":
        print("YES")
        t=1
        break
if not t:
    print("NO")
        
