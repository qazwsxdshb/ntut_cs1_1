price=[[2.1,3.02,4.39,4.97,5.63],[2.1,2.68,3.61,4.01,4.50]]
ch=1
if((lambda a:(True if (a>=7 and a<=9) else False))(int(input()))):
    ch=0
# def real_cal(price: list,pow: int):
#     if(pow<=120):
#         return price[0]*pow
#     elif(pow<=330): 
#         return price[0]*120+price[1]*(pow-120)
#     elif(pow<=500): 
#         return price[0]*120+price[1]*210+price[2]*(pow-330)
#     elif(pow<=700): 
#         return price[0]*120+price[1]*210+price[2]*170+price[3]*(pow-500)
#     else:
#         return price[0]*120+price[1]*210+price[2]*170+price[3]*200+price[4]*(pow-700)
def cal(price: list,pow: int):
    if(pow<=120):
        return price[0]*pow
    elif(pow<=330): 
        return price[1]*pow
    elif(pow<=500): 
        return price[2]*pow
    elif(pow<=700): 
        return price[3]*pow
    else:
        return price[4]*pow
b=int(input())
y=int(input())
print(cal(price[ch],y)-0.6*(b-y if b>y else 0))