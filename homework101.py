a=[]
for _ in range(5):
    a.append(input())
print("Name:",a[0],"\nID:",a[1],"\nAverage:",sum(int(i) for i in a[2:])//3,"\nTotal:",sum(int(i) for i in a[2:]),sep="")