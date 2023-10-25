try:
    while 1:
        BMI=(lambda height,weight:"%.2f"(float(weight)/float(height)**2))(input().split())
        print(BMI)
except:
    print("exit")