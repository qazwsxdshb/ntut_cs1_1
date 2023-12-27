import math
cla,sub={},[]
for _ in range(int(input())):
    start=input().split()
    sub.append(start)
    for _ in range(int(start[2])):
        tmp=input().split()
        try:cla[start[0]+" "+start[1]+" "+tmp[0]]=tmp[1]+" "+tmp[2]
        except:cla[start[0]+" "+start[1]+" "+tmp[0]]=tmp[1]

tmp=[]
for i in cla:
    if i.split()[2][:6]+i.split()[1][:3] not in tmp:
        tmp.append(i.split()[2][:6]+i.split()[1][:3])
tmp=sorted(tmp,key=lambda x:(int(x[3:6]),int(x[:3],int(x[6:-1]))))
def all(arr,key):
    for i in arr:
        if(i[0] == key):return False
    return True
fin=[]
for i in tmp:
    print(i[3:6],i[:3],i[6:])
    try:
        if(i[6:] not in fin[0][3]):fin=[]
    except:None
    ans,bye=[],0
    for u in cla:
        if(u.split()[2][:6] in i[:6] and u.split()[1][:3] in i[6:]):ans.append(u.split()[2]+" "+cla[u]+" "+u.split()[0][-1])
    for u in ans:
        try:
            err=0
            if(len(u.split())==4):
                t=(math.ceil(int(u.split()[1])*0.7+int(u.split()[2])*0.3)*int(u.split()[-1]))
                for p in range(len(fin)):
                    if(u.split()[0] in fin[p][0] and i[6:] in fin[p][3]):
                        fin[p][1]=(fin[p][1]+t)
                        fin[p][2]+=int(u.split()[-1])
                        err=1
                if(err==0):
                    fin.append([u.split()[0],t,int(u.split()[-1]),i[6:]])
            else:
                for p in range(len(fin)):
                    if(u.split()[0] in fin[p][0] and i[6:] in fin[p][3]):
                        fin[p][1]=(fin[p][1]+int(u.split()[1])*int(u.split()[-1]))
                        fin[p][2]+=int(u.split()[-1])
                        err=1
                if(err==0):fin.append([u.split()[0],int(u.split()[1])*int(u.split()[-1]),int(u.split()[-1]),i[6:]])
        except:
            if all(fin,u.split()[0]):bye+=1
    for u in range(len(fin)):
        fin[u][1]=((fin[u][1])/fin[u][2])
    fin=sorted(fin,key=lambda x:int(x[1]),reverse=True)
    # print(fin,len(fin))
    for i in range(3):
        tmp1,co=0,0
        for p in cla:
            if(p.split()[-1]==fin[i][0]):
                if(cla[p].split()[-1]=="w"):co+=1
                tmp1+=1
        if(i==0):print(fin[i][0]," ",int(fin[i][1])," 1% ",co//tmp1,"%",sep="")
        else:
            if((100*i/(len(fin)))%1==0):
                # print(fin[i][0]," ",math.ceil(fin[i][1]) if fin[i][1]%1>=0.5 else int(fin[i][1])," ",(int(100*i/(len(fin))))+1,"% ",co//tmp1,"%",sep="")
                print(fin[i][0]," ",int(fin[i][1])," ",(int(100*i/(len(fin)+bye)))+1,"% ",co//tmp1,"%",sep="")
            else:
                # print(fin[i][0]," ",math.ceil(fin[i][1]) if fin[i][1]%1>=0.5 else int(fin[i][1])," ",(int(100*i/(len(fin))))+1,"% ",co//tmp1,"%",sep="")
                print(fin[i][0]," ",int(fin[i][1])," ",(int(100*i/(len(fin)+bye)))+1,"% ",co//tmp1,"%",sep="")
sub=sorted(sub,key=lambda x:(int(x[0]),int(x[1])))
for i in sub:
    tmp,su,x,bye=[],0,0,0
    print(i[0],i[1][:3])
    for u in cla:
        if(str(u[:8])==i[0]+" "+i[1][:-1]):
            try:
                if(len(cla[u].split())==2):
                    t=math.ceil(int(cla[u].split()[0])*0.7+int(cla[u].split()[1])*0.3)
                    tmp.append([u,t])
                    su+=t
                else:
                    tmp.append([u,int(cla[u])])
                    su+=int(cla[u])
                x+=1
            except:bye+=1
    tmp,adv,sd=sorted(tmp,key=lambda x:x[1],reverse=True),su//x,0
    for u in tmp:sd+=((u[1]-adv)**2)
    try:print(tmp[0][1]," ",adv," ",tmp[-1][1]," ",int(bye/(x+bye)*100),"%",sep="")
    except:print(tmp[0][1]," ",adv," ",tmp[-1][1]," 0%",sep="")
    for u in range(3):
        if(u==0):print(tmp[u][0].split()[-1],tmp[u][-1],"1% ")
        else:print(tmp[u][0].split()[-1]," ",tmp[u][-1]," ",(int(100*u/(x+bye)))+1,"%",sep="")

key,tmp,x=input(),[],{}
for i in cla:
    if(i.split()[0]==key):
        try:x[i.split()[2][3:6]]+=1
        except:x[i.split()[2][3:6]]=1
        try:dd=list(map(int,cla[i].split()))
        except:pass
        try:
            if(len(dd)==2):
                tmp.append([i.split()[2],math.ceil(dd[0]*0.7+dd[1]*0.3)])
            else:
                tmp.append([i.split()[2],math.ceil(dd[0])])
        except:None
tmp=sorted(tmp,key=lambda x:x[1],reverse=True)
tmp1=[]
for i in x:
    tmp1.append([i,x[i]])
tmp1=sorted(tmp1,key=lambda x:x[1])
if(len(tmp1)>=2):
    print(tmp[0][0],tmp[1][0],tmp1[-1][0],tmp1[-2][0])
else:
    print(tmp[0][0],tmp[1][0],tmp1[-1][0])