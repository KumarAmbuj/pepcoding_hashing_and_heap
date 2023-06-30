def findlongestconsecutive(arr):
    hash={}

    for x in arr:
        hash[x]=True

    for x in arr:
        if x-1 in hash:
            hash[x]=False

    print(hash)

    finalele=0
    finallen=0

    for x in arr:

        if hash[x]==True:

            ele=x
            count=0
            while(x in hash):
                count+=1
                x+=1

            if count>finallen:
                finallen=count
                finalele=ele
    print(finalele,finallen)


arr=[10,5,9,1,11,8,6,15,3,12,2]
findlongestconsecutive(arr)


