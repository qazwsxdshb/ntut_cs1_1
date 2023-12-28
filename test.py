def fun(data,start,end,path,finalans):
    temp=[]
    if start in path:pass
    else:
        if start==end:
            return path+[end]
        for keys in data:
            if keys==start:
                for i in data[keys]:
                    temp.append(fun(data,i,end,path+[start],finalans)) 
                for i in temp:
                    if i not in finalans:
                        finalans.append(i)

            if start in data[keys]:
                temp.append(fun(data,keys,end,path+[start],finalans))
                for i in temp:
                    if i not in finalans :
                        finalans.append(i)
    if(len(finalans)!=0):
        return finalans


num,start,end=input().split()
bre=input().split()
data={}
for i in range(int(num)):
    a=input().split()
    try:
        data[a[0]]=data[a[0]]+[a[1]]
    except:
        data[a[0]]=[a[1]]
print(data)
ans=fun(data,start,end,[],[])
print(ans)