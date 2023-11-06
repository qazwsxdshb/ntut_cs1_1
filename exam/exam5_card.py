def cal(type,number):
    tmp=[]
    for i in number:
        if(i=="A"):tmp.append(1)
        elif(i=="J"):tmp.append(11)
        elif(i=="Q"):tmp.append(12)
        elif(i=="K"):tmp.append(13)
        else:tmp.append(int(i))
    x=""
    for i in sorted(tmp):x+=str(i)
    if(len(set(type))==1 and (x in "12345678910111213" or x in "110111213" or x in "12111213" or x in"1231213" or x in "123413")):return 9
    if(len(set(number)))==2:
        for i in number:
            if(number.count(i)==4):return 8
            elif(number.count(i)==3):return 7
    if(len(set(type))==1):return 6
    if(x in "12345678910111213" or x in "110111213" or x in "12111213" or x in"1231213" or x in "123413"):return 5
    if(len(set(number))==3):
        for i in number:
            if(number.count(i)==3):return 4
        return 3
    if(len(set(number))==4):return 2
    return 1


ans,b=[],[]
x=0
for _ in range(2):
    a=input().split()
    type,number=[],[]
    b+=a
    for i in a:
        type.append(i[-1])
        number.append(i[:-1])
    for i in range(len(number)):
        if(number[i] not in "A2345678910JQK" or type[i] not in "SHDC" or number[i]=="1"):x=2
    if(x==0):
        ans.append(cal(type,number))
if(x==0):
    while b:
        if(b.pop(0) in b):
            print("Duplicate deal")
            x=1
            break
if(x==0):
    print(max(ans))
if(x==2):
    print("Error input")