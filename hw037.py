import math

stu,cla,xx={},[],[]
for _ in range(int(input())):
    tmp1=input().split()
    cla.append([tmp1[0],tmp1[1],int(tmp1[-1])])
    for i in range((int(tmp1[-1]))):
        tmp2=input().split()
        xx.append(tmp2[0][:6])
        stu[tmp1[0]+" "+tmp1[1]+" "+tmp2[0]]=tmp2[1:]

def search(key,stu,ans=[],cla={},like=0):
    bye,ppp=0,{}
    for i in stu:
        if all(u in i.split() for u in key) or (like==1 and str(key[0]) in str(i.split()[2]) and str(key[1]) in str(i.split()[1])):
            ppp[i.split()[2]]=0
            try:cla[i.split()[-1][3:6]]+=1
            except:cla[i.split()[-1][3:6]]=1
            try:
                if len(stu[i])>=2:ans.append([i.split()[2],math.ceil(int(stu[i][0])*0.7+0.3*int(stu[i][1])),int(i.split()[0][-1])])
                else:ans.append([i.split()[2],int(stu[i][0]),int(i.split()[0][-1])])
            except:
                ppp[i.split()[2]]+=1
                bye+=1
    return ans,cla,bye,ppp

# part 1
for i in sorted([uu for uu in set(xx)],key=lambda x:(int(x[3:]),int(x[:3]))):
    for u in sorted(list(set(list(int(uu[1][:-1]) for uu in cla)))):
        tmp=search([i,u],stu,[],{},1)
        if(len(tmp[0])!=0):
            print(i[3:],i[:3],u)
            co,arr,p,ans,zzz=0,sorted(tmp[0],key=lambda x:int(x[0])),0,[],0
            tmp1=arr[0][0]
            for z in arr:
                if(z[0]!=tmp1):
                    ans.append([tmp1,int(co/p),zzz])
                    tmp1,co,p,zzz=z[0],z[1]*z[2],z[2],1
                else:
                    try:co+=z[1]*z[2];p+=z[2];zzz+=1
                    except:None
            ans.append([tmp1,int(co/p),zzz])
            ans=sorted(sorted(ans,key=lambda x:int(x[0])),key=lambda x:x[1],reverse=True)
            for uu in range(3):
                print(*ans[uu][:-1],str(int(100*uu/len(tmp[3]))+1)+"%",str(int(100*int(tmp[3][ans[uu][0]])/(int(tmp[3][ans[uu][0]])+ans[uu][-1])))+"%")

# part 2
for i in sorted(cla,key=lambda x:(int(x[0]),int(x[1][:-1]))):
    print(i[0],i[1][:-1])
    tmp1=search([i[0],i[1]],stu,[],{},0)
    tmp2=sorted(sorted(tmp1[0],key=lambda x:int(x[0])),key=lambda x:x[1],reverse=True)
    print(tmp2[0][1],sum(u[1] for u in tmp2)//len(tmp2),tmp2[-1][1],str(int(tmp1[2]*100/(len(tmp1[0])+tmp1[2])))+"%")
    for u in range(3 if len(tmp2)>=3 else len(tmp2)):print(*tmp2[u][:-1],str(int(100*u/(len(tmp1[0])+tmp1[2]))+1)+"%")

# part 3
tmp=search([input()],stu,[],{},0)
x=sorted(tmp[0],key=lambda x: x[1],reverse=True)[:2]
y=sorted(tmp[1].items(),key=lambda x:x[1],reverse=True)
print(x[0][0]," ",x[1][0]," ",y[0][0]," "+y[1][0] if(len(y)>=2) else "",sep="")