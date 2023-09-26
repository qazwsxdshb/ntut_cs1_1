pri=[[380,0.9,0.85,0.8],[1200,0.95,0.85,0.8],[180,0.85,0.8,0.7]]
co,ans=0,0
x=[]
for i in range(3):
    x.append(input())
for i in x:
    i=int(i)
    if(i<=20 and i>=11):
        ans+=i*pri[co][1]*pri[co][0]
    elif(i>=21 and i<=30):
        ans+=i*pri[co][2]*pri[co][0]
    elif(i>=31):
        ans+=i*pri[co][3]*pri[co][0]
    else:
        ans+=i*pri[co][0]
    co+=1
print(int(ans))