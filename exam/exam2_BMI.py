ans=[]
try:
    while 1:
        height,weight=map(int,input().split())
        if(0.5>height*0.01 or height*0.01>2.5):
            ans.append("Input Height Error")
        elif(20>weight*0.454 or weight*0.454>300):
            ans.append("Input Weight Error")
        else:
            BMI=(weight*0.454)/(height*0.01)**2
            if(BMI>24.00):
                ans.append("BMI too high")
            elif(18.50>BMI):
                ans.append("BMI too low")
            else:
                ans.append("%.2f" %(int(BMI*100)/100))
except:
    for i in ans:print(i)