a,x=int(input()),int(input())
tmp,ans=[],""
for i in range(1,x+1):
    tmp.append(str(i))
    if(a!=1):ans+="_"*(x-i)
    for u in tmp:ans+=u if (a!=3) else u[::-1]
    for u in tmp[:-1][::-1]:ans+=u if (a!=3) else u[::-1]
    if(a!=1):ans+="_"*(x-i)
    ans+="\n"
print(ans[:-1][::-1] if a==3 else ans[:-1]) if 1<=a and a<=3 and 3<=x and x<=50 else None