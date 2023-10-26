def Is_True(tmp):
    if(tmp=="J" or tmp=="Q" or tmp=="K"):return 0.5
    elif(tmp=="A"):return 1
    return float(tmp)

user,pc,co,tmp=Is_True(input()),Is_True(input()),0,0
while pc<=10.5 and user<=10.5 and (co==0 or tmp==0):
    if(co==0):
        if input()[0]=="Y":user+=Is_True(input())
        else:co=1
    if((user>pc or pc<=8) and tmp==0 and user<=10.5):pc+=Is_True(input())
    else:tmp=1
    if(co==1 and pc>user and pc<=10.5):
        print("computer win")
        co=2
        break
    if(co==1 and tmp==1 ):break

if(pc==user):print("it's a tie")
elif(pc>10.5 or (user>pc and user<=10.5)):print("player win")
elif(co!=2):print("computer win")