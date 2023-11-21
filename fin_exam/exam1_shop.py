tmp,ans=[],[]
for _ in range(int(input())):
    tmp.append(input().split())
for i in tmp:
    if(int(i[1])>=70):
        ans.append([i[0],int(int(i[1])*0.8//1)])
for i in sorted(ans,key=lambda x:x[1],reverse=True):
    print(i[0],i[1])
