def ca(N):
    if(3<=N<=49 and N%2==1):
        return N
    else:
        print("error")
        return -1
a=int(input())
if(a==1):
    x=ca(int(input()))
    if(x!=-1):
        for i in range(1,1+x):
            print("#"*(x-i),"*"*((i-1)*2+1),"#"*(x-i),sep="")
elif(a==2):
    x=ca(int(input()))
    if(x!=-1):
        for i in range(x,0,-1):
            print("#"*(x-i),"*"*((i-1)*2+1),"#"*(x-i),sep="")
elif(a==3):
    x=ca(int(input()))
    if(x!=-1):
        tmp=1
        while x+2!=tmp:
            print(" "*((x-tmp)//2),"*"*tmp,sep="")
            tmp+=2
        tmp-=2
        while 1!=tmp:
            tmp-=2
            print(" "*((x-tmp)//2),"*"*tmp,sep="")
elif(a==4):
    x=ca(int(input()))
    if(x!=-1):
        tmp,tail=1,0
        while x+2!=tmp:
            print(" "*((x-tmp)//2),"*"*tmp," "*((x-tmp)),"-"*tail,sep="")
            tmp+=2
            tail+=1
        tmp-=2
        tail-=1
        while 1!=tmp:
            tmp-=2
            tail-=1
            print(" "*((x-tmp)//2),"*"*tmp," "*((x-tmp)),"-"*tail,sep="")