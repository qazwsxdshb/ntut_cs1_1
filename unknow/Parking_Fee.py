start,end=[],[]
for i in range(3):
    start.append([int(u) for u in input().split(":")])
    end.append([int(u) for u in input().split(":")])

for i in range(3):
    x=((end[i][0]-start[i][0])*60+end[i][1]-start[i][1])
    if(end[i][0]>24 or start[i][0]>24 or end[i][1]>60 or start[i][1]>60 or end[i][0]<0 or start[i][0]<0 or end[i][1]<0 or start[i][1]<0):
        print("error")
    elif(x<120):
        print(x//30*30)
    elif(x<240):
        print(120+(x-120)//30*40+40 if x%30!=0 else 120+(x-120)//30*40)
    else:
        print(280+(x-240)//30*60+60 if x%30!=0 else 280+(x-240)//30*60)