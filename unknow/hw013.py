tmp,ans=0,0
for i in range(4):
    x=int(input())
    ans+=x
    if(x+tmp==10 and i==3):
        ans+=int(input())
    tmp=x
print(ans)