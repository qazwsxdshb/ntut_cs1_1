def solution(mx):
    tmp1=[]
    for i in range(len(mx)):
        tmp=[]
        for u in range(len(mx[0])-1,-1,-1):
            tmp.append(mx[u][i])
        tmp1.append(tmp)
    return tmp1

co=int(input())
a=input()
ans=[]
for i in range(co):
    ans.append(input().split())
for i in a:
    if(i=="L"):
        for _ in range(3):
            ans=solution(ans)
    else:
        ans=solution(ans)
tmp=""
for i in ans:
    for u in i:
        tmp+=u+" "
    tmp=tmp[:-1]+"\n"
print(tmp)