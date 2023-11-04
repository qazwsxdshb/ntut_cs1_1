def check(ans):
    if(ans=="A"):return 1
    elif(ans=="J" or ans=="Q" or ans=="K"):return 0.5
    return int(ans)

co=int(input())
money,point=list(map(int,input().split())),list(map(check,input().split()))

for i in range(co):
    q=1
    while q:
        q=input()
        if(len(q)==1):q=0
        else:point[i+1]+=check(q.split()[-1])
        if(point[i+1]>10.5):
            point[i+1]=0
            q=0
        if(point[i+1]==10.5):break
tmp=[1]*(len(point))
def computer_show(point):
    co,tim=0,0
    while point[0]<10.5 and co!=len(point)-1:
        ans=0
        for i in range(1,len(point)):
            if(point[0]>=point[i]):
                ans+=-1*money[i-1]
                co+=tmp[i-1]
                tmp[i-1]=0
            else:ans+=money[i-1]
        if(tim==1 or 10.5==min(point[1:])):break
        if(co!=len(point)-1 and 10.5!=min(point[1:])):
            point[0]+=check(input())
        if(point[0]>min(point[1:]) and (0!=min(point[1:]) or sorted(set(point[1:]))[1]<point[0])):tim=1
    return ans

ans=computer_show(point)
point[0] = 0 if point[0]>10.5 else point[0]

for i in range(1,len(point)):
    if(point[0]>=point[i] and point[i]!=10.5):
        tmp[i-1]=0
        print("Player",i," ",str(-1*money[i-1]),sep="")
    else:
        print("Player",i," +",str(money[i-1]),sep="")

print("Computer ", "+" if ans<0 else "",str(-1*ans),sep="")
