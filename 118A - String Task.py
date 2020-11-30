s=input()
v={'a',"A",'e','o','i','u','E','I','O','U','y',"Y"}
ans=""
for i in s:
    if i not in v:
        if i.isupper():
            ans=ans+"."+i.lower()
        else:
            ans=ans+"."+i
print(ans)
