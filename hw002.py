import math
a=int(input())
b=int(input())
c=int(input())

print("%.1f" %(((-b)+math.sqrt(b*b-4*a*c))/(2*a)))
print("%.1f" %(((-b)-math.sqrt(b*b-4*a*c))/(2*a)))
