def check(tmp):
    if(tmp=="K"):return 0.5
    elif(tmp=="Q"):return 0.5
    elif(tmp=="J"):return 0.5
    elif(tmp=="A"):return 1.0
    else:return float(tmp)

type=int(input())
money=input().split()
point=list(map(check,input().split()))
for i in range(1,1+type):
    try:
        co=0
        while 1:
            a,b=input().split()
            point[i]+=check(b)
            if(point[i]>10.5):
                point[i]=0
                break
            co+=1
            if(point[i]==10.5 or co==4):
                point[i]=10.5
                break
    except:None
while 1:
    if(point[0]>min(point) or point.count(min(point))>=2):
        break
    point[0]+=check(input())
    if(point[0]>10.5):
        point[0]=0
        break
for i in range(len(point)-1):
    if(point[i+1]==10.5):
        print("Player",i+1," +",money[i],sep="")
    elif(point[0]>=point[i+1]):
        print("Player",i+1," ",-int(money[i]),sep="")
    else:
        print("Player",i+1," +",str(money[i]),sep="")
    