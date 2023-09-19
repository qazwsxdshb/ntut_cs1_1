fee=[[0.08,0.139,0.135,1.128,1.483,250],[0.07,0.130,0.121,1.128,1.483,200],[0.06,0.108,0.101,1.128,1.483,150],[0.05,0.100,0.090,1.128,1.483,0]]
b=[183,383,983,1283]
x=[1,3,5,0]
ans=[int(input()) for _ in range(6)]
a=[]
for u in range(4):
    tmp,co=0,0
    for i in ans:
        if(co==5):
            tmp+=(i-x[u])*fee[u][co] if 0<=(i-x[u])*fee[u][co] else 0
        else:
            tmp+=i*fee[u][co]
        co+=1
    a.append(tmp if tmp>b[u] else b[u])
    
print(int(a[a.index(min(a))]))
print(b[a.index(min(a))])