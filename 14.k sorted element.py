class Pair:
    def __init__(self,li,di,val):
        self.li=li
        self.di=di
        self.val=val


def Heap():
    heap=[]
    return heap
def makeheap(heap):
    n=len(heap)

    for i in range((n-1)//2,-1,-1):
        heapify(heap,i,n)
def heapify(heap,i,n):
    min=i

    l=2*i+1
    r=2*i+2

    if l<n and heap[l].val<heap[min].val:
        min=l

    if r<n and heap[r].val<heap[min].val:
        min=r

    if min !=i:
        heap[i],heap[min]=heap[min],heap[i]
        heapify(heap,min,n)
def Add(heap,x):
    heap.append(x)

    n=len(heap)
    i=n-1

    while(i>0 and heap[i].val< heap[(i-1)//2].val):
        heap[i],heap[(i-1)//2]=heap[(i-1)//2],heap[i]
        i=(i-1)//2

def extractmin(heap):
    x=heap[0]
    n=len(heap)
    heap[0]=heap[n-1]
    heap.pop()

    n=len(heap)
    heapify(heap,0,n)
    return x

def Size(heap):
    return len(heap)

def mergeksorted(arr):

    ans=[]

    heap=Heap()

    for i in range(len(arr)):

        Add(heap,Pair(i,0,arr[i][0]))


    while(Size(heap)):
        p=extractmin(heap)
        ans.append(p.val)

        p.di+=1

        if p.di<len(arr[p.li]):

            val=arr[p.li][p.di]
            p.val=val
            Add(heap,p)
    print(ans)

arr=[[10,20,30,40],[5,9,12,18,32],[11,15,17]]

mergeksorted(arr)




