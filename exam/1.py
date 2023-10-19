a=int(input())
b=int(input())
if(a==1):
    for u in range(1,1+b):
        print(str(u)*(u)+"#"*(b-u))
# elif(a==2):
    # for u in range(b):
        # print(("#"*(b+b-1))
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
    for i in range(1,b*2):
        print("^"*(b-i),end="")
        for u in range(i,0,-1):
            print(u%(b+1),end="")
        print("^"*(b-i))