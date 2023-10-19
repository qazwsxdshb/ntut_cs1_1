a=int(input())
if(a==1):
    tmp=""
    for i in range(1,int(input())+1):
        tmp+=str(i)
        print(tmp,tmp[:-1][::-1],sep="")
elif(a==2):
    tmp=""
    x=int(input())
    for i in range(1,x+1):
        tmp+=str(i)
        print("_"*(x-i),tmp,tmp[:-1][::-1],"_"*(x-i),sep="")
elif(a==3):
    ans=""
    tmp=""
    x=int(input())
    for i in range(1,x+1):
        tmp+=str(i)
        ans+="_"*(x-i)+tmp+tmp[:-1][::-1]+"_"*(x-i)+"\n"
    print(ans[:-1][::-1])