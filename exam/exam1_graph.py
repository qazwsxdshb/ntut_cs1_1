a=input()
x=int(input())
if(a=="1"):
    for i in range(1,1+x):
        print(str(i)*(i),"#"*(x-i),sep="")
elif(a=="2"):
    for i in range(1,1+x):
        print("#"*(2*(x-i)),end="")
        for u in range(1,i+1):
            print(u,end="")
        for u in range(i-1,0,-1):
            print(u,end="")
        print()
elif(a=="3"):
    for i in range(1,1+x):
        for u in range(1,i+1):
            print(u,end="")
        print("^"*((x-i)))
    for i in range(x,0,-1):
        for u in range(i,0,-1):
            print(u,end="")
        print("^"*((x-i)))
elif(a=="4"):
    for i in range(1,1+x):
        print("^"*(x-i),end="")
        for u in range(i,0,-1):
            print(u,end="")
        for u in range(2,i+1):
            print(u,end="")
        print("^"*(x-i),end="")
        print()
    for i in range(x-1,0,-1):
        print("^"*(x-i),end="")
        for u in range(i,0,-1):
            print(u,end="")
        for u in range(2,i+1):
            print(u,end="")
        print("^"*(x-i),end="")
        print()