def findcommonelement(arr1,arr2):

    hash={}

    for x in arr1:
        hash[x]=hash.get(x,0)+1

    for x in arr2:

        if x in hash:
            print(x,end=' ')
            del hash[x]



arr1=[1,1,2,2,2,3,5]
arr2=[1,1,1,2,2,4,5]

findcommonelement(arr1,arr2)