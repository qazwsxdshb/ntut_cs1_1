a=int(input())
b=int(input())
c=int(input())
def str_to_arr(ans1):
    tmp1=[]
    tmp=""
    for i in ans1:
        if(i!="+" and i!="-" and i!="i"):
            tmp+=i
        else:
            tmp1.append(tmp)
            tmp1.append(i)
            tmp=""
    tmp1.append(tmp)
    for i in tmp1:
        if(len(i)==0):
            tmp1.remove('')
    co=0
    for i in tmp1:
        if("e" in i):
            tmp1=tmp1[co+3:]
            tmp1.insert(0,0)
        co+=1
    return tmp1

ans1=str_to_arr(str(((-b+((b**2-(4*a*c))**0.5))/(2*a))).replace("(","").replace(")","").replace("j","i"))
ans2=str_to_arr(str(((-b-((b**2-(4*a*c))**0.5))/(2*a))).replace("(","").replace(")","").replace("j","i"))
for i in ans1:
    try:
        print("%.1f" %float(i),end="")
    except:
        print(i,end="")
print()
for i in ans2:
    try:
        print("%.1f" %float(i),end="")
    except:
        print(i,end="")