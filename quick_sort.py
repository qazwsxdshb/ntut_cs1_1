def quick(arr):
    if(len(arr)<=1):return arr
    tmp,co,target=[],0,arr.pop(0)
    while len(arr)!=co:
        if(arr[co]>=target):tmp.append(arr.pop(co))
        else:co+=1
    print(arr,target,tmp)
    return quick(arr)+[target]+quick(tmp)

print(quick(list(map(int,input().split()))))