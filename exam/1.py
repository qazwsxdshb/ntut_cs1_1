a=int(input())
b=int(input())
if(a==1):
    for u in range(1,1+b):
        print(str(u)*(u)+"#"*(b-u))
elif(a==2):
    for u in range(b):
        print("#"*(b*2-2-u*2),end="")
        for i in range(1,2+u):
            print(i,end="")
        for i in range(u,0,-1):
            print(i,end="")
        print()
elif(a==3):
    for i in range(1,b+1):
        tmp=""
        for u in range(i):tmp+=str(u+1)
        print(tmp+"^"*(b-i))
    for i in range(b,0,-1):
        tmp=""
        for u in range(i,0,-1):tmp+=str(u)
        print(tmp+"^"*(b-i))
elif(a==4):
    ans=''
    for i in range(1,b+1):
        ans+="^"*(b-i)
        for u in range(i,0,-1):
            ans+=str(u%(b+1))
        for u in range(1,i,1):
            ans+=str(u+1%(b+1))
        ans+="^"*(b-i)+"\n"
    print(ans[:-1]+ans[:-(b*2)][::-1])