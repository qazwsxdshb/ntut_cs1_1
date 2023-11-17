# mybmi.py
#合法範圍:體重(3<=~ <=200),身高(0.50<=~<=2.50)。
def computeBMI(kg, M):
    if 3>kg or kg>200: #錯誤,範圍判斷錯誤
        return -1
    if 0.5>M or M>2.5:
            return -1
    BMI = round(kg/(M*M),2) #錯誤,四捨五入取兩位小數
    BMI = ((100*kg/(M*M))//1)/100
    return BMI

