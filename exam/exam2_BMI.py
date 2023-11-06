try:
    while 1:
        height,weight=map(int,input().split())
        if(0.5>height*0.01 or height*0.01>2.5):
            print("Input Height Error")
        elif(20>weight*0.454 or weight*0.454>300):
            print("Input Weight Error")
        else:
            BMI=(weight*0.454)/(height*0.01)**2
            if(BMI>24.00):
                print("BMI too high")
            elif(18.50>BMI):
                print("BMI too low")
            else:
                print(int(BMI*100)/100)
except:None