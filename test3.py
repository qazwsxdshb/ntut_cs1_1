def noOfDigits(x,ans="",tmp=""):
    if(len(x)==1):return ans+x+" "
    for i in range(len(x)):
        tmp+=noOfDigits(x.replace(x[i],""),ans+x[i])
    return tmp
print(noOfDigits(input()))