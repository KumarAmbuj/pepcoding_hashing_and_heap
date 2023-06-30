def getcommonelement(arr1,arr2):
    hash={}

    for x in arr1:
        hash[x]=hash.get(x,0)+1

    for x in arr2:
        if x in hash and hash[x]>0:
            print(x,end=' ')
            hash[x]-=1

arr1=[1,1,2,2,2,4,5]
arr2=[1,1,1,2,2,3,5]

getcommonelement(arr1,arr2)