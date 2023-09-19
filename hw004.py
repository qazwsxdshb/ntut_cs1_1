hi=float(input())
kg=float(input())
bmi=int(float(kg/(hi*hi))*1000)
if(bmi%10==5 and ((bmi//10)%10)%2==1):
    print("%.2f" %((bmi+10)//10/100)) 
else:
    print("%.2f" %((bmi//10)/100))