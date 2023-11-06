n=int(input())
si=input()
ans,tmp=[],[]
for i in range(1,1+n**2):
    tmp.append(i)
    if(i%n==0):
        ans.append(tmp)
        tmp=[]
def tr(arr):
    ans,tmp=[],[]
    for i in range(len(arr)-1,-1,-1):
        for u in range(len(arr)):
            tmp.append(arr[u][i])
        ans.append(tmp)
        tmp=[]
    return ans
def up_down(arr):
    ans=[]
    for i in range(len(arr)-1,-1,-1):
        ans.append(arr[i])
    return ans
def right_left(arr):
    ans=[]
    for i in range(len(arr)):
        ans.append(arr[i][::-1])
    return ans
if(si=="1"):
    ans=tr(ans)
elif(si=="2"):
    for _ in range(3):ans=tr(ans)
elif(si=="3"):
    ans=up_down(ans)
elif(si=="4"):
    ans=right_left(ans)
for i in ans:
    for u in i:
        print(u,end=" ")
    print()