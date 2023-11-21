ans=[]
for _ in range(int(input())):
    tmp=input().split()
    if(sum(list(int(i) for i in tmp[1:]))/4>=60):
        ans.append([tmp[0],int(sum(list(int(i) for i in tmp[1:]))/4//1)])
for i,u in sorted(ans,key=lambda i:i[1]):print(i,u)