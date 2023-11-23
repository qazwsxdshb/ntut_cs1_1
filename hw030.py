def Solution(tmp,index=0):
    if(tmp==0 or tmp==1):
        return index
    if(tmp%2==0):
        return Solution(tmp//2,index+1)
    else:
        return Solution((tmp+1)//2,index+1)
ans=[]
while 1:
    tmp=0
    for i in range(int(input(),2)+1):
        tmp+=Solution(i)
    ans.append(bin(tmp)[2:])
    if input()=="-1":break
print(ans)
for i in ans:
    print("0"*(14-len(i))+i)