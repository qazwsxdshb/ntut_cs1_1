tmp=[]
for _ in range(int(input())):
    tmp+=[int(u) for u in input().split()]

ans=[0 for _ in range(min(tmp),max(tmp))]
for i in range(0,len(tmp),2):
    for u in range(tmp[i]+abs(min(tmp)),tmp[i+1]+abs(min(tmp))):
        ans[u]=1
print(sum(ans))
