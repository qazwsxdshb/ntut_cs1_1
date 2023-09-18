fee=[[0.08,0.139,0.135,1.128,1.483],[0.07,0.130,0.121,1.128,1.483],[0.06,0.108,0.101,1.128,1.483]]
b=[183,383,983]
ans=[]
for i in input().split():
    ans.append(int(i))
a=[]
c=int(input())
for u in range(3):
    tmp=0
    co=0
    for i in ans:
        tmp+=i*fee[u][co]
        co+=1
    a.append(tmp)
print(a)
for _ in range(2):
    if(b[a.index(min(a))]>c):
        a.pop(a.index(min(a)))
print(b[a.index(min(a))])
