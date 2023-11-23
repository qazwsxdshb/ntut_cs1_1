def Solution(tmp,index=0):
    if(tmp==0 or tmp==1):
        return index
    if(tmp%2==0):
        return Solution(tmp//2,index+1)
    else:
        return Solution((tmp+1)//2,index+1)
ans=[]
while 1:
    tmp,x=0,input()
    if x=="-1":break
    for i in range(int(x,2)+1):
        tmp+=Solution(i)
    ans.append(bin(tmp)[2:])
for i in ans:
    print("0"*(14-len(i))+i)