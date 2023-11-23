def gray(n,k,ans=""):
    if(n==0):return ans
    return gray(n-1,k,ans+"0") if k<2**(n-1) else gray(n-1,2**n-1-k,ans+"1")
try:
    while 1:
        n,k=map(int,input().split())
        print(gray(n,k))
except:None