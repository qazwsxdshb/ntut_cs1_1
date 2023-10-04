def BMI():
    hi,kg=[float(i) for i in input().split()]
    bmi=float(kg/(hi*hi))
    return bmi

def cal(bmi):
    bmi=bmi*1000
    if(bmi%10>5):
        return ("%.2f" %(((bmi+10)//10)/100))
    elif(bmi%10<5):
        return ("%.2f" %((bmi//10)/100))
    elif(bmi%10==5 and ((bmi//10)%10)%2==1):
        return ("%.2f" %((bmi+10)//10/100))
    elif(bmi%10==5 and ((bmi//10)%10)%2==0):
        return ("%.2f" %((bmi//10)/100))

if __name__=="__main__":
    ans,ans2=[],[]
    for i in range(int(input())):
        x=BMI()
        ans.append(float(x))
        ans2.append(float(cal(x)))
    ans=sorted(ans)
    print(cal(max(ans)),"\n",cal(min(ans)),sep="")
    print(cal(ans[len(ans)//2]) if len(ans)%2==1 else cal(((float(ans[len(ans)//2])+float(ans[(len(ans)//2)-1]))/2)))
    tmp=0
    ans2=sorted(ans2)
    for i in ans2:
        if(tmp<ans2.count(i)):
            a=i
            tmp=ans2.count(i)
    print(a)