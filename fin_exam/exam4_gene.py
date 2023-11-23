pre=[2,3,5,7,11,13,17,19,23,29,31,37,41,43]
ans,x=[],0
start=input()
end=input().split()
string=input()
def cal(ans):
    for i in ans:
        if(i not in "ATCG"):
            return 1
    return 0
x=cal(start)
if(x==0):
    x=cal(string)
if(x==0):
    for i in end:
        x=cal(i)
        if(x==1):break
while string and x!=1 and x!=2:
    if(string[:len(start)]!=start):
        x=1
        break
    string=string[len(start):]
    for u in pre:
        d=0
        for i in end:
            if(string[u:u+len(i)]==i):
                ans.append(string[:u])
                string=string[u+len(i):]
                d=1
                break
        if(d==1):break
        if(u>len(string)):
            x=2
            print("No gene")
            break
if(x!=1 and x!=2):
    for i in sorted(ans,key=lambda x:(len(x),x)):
        print(i)
elif(x==1):print("Input error")