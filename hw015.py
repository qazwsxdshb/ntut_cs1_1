def BMI():
    hi,kg=[float(i) for i in input().split()]
    bmi=int(float(kg/(hi*hi))*1000)
    return cal(bmi)

def cal(bmi):
    if(bmi%10>5):
        return ("%.2f" %(((bmi+10)//10)/100))
    elif(bmi%10<5):
        return ("%.2f" %((bmi//10)/100))
    elif(bmi%10==5 and ((bmi//10)%10)%2==1):
        return ("%.2f" %((bmi+10)//10/100))
    elif(bmi%10==5 and ((bmi//10)%10)%2==0):
        return ("%.2f" %((bmi//10)/100))

if __name__=="__main__":
    ans=[]
    for i in range(int(input())):
        ans.append(BMI())
    print(max(ans))
    print(min(ans))
    ans=sorted(ans)
    print(ans[len(ans)//2] if len(ans)%2==1 else cal((float(ans[len(ans)//2])+float(ans[(len(ans)//2)-1]))/2*1000))
    tmp=0
    for i in ans:
        if(tmp<ans.count(i)):
            a=i
            tmp=ans.count(i)
    print(a)