def Heap():
    heap=[]
    return heap

def makeheap(heap):
    n=len(heap)
    for i in range((n-1)//2,-1,-1):
        heapify(heap,i,n)
def heapify(arr,i,n):
    min=i

    l=2*i+1
    r=2*i+2

    if l<n and arr[l]<arr[min]:
        min=l
    if r<n and arr[r]<arr[min]:
        min=r

    if min !=i:
        arr[i],arr[min]=arr[min],arr[i]
        heapify(arr,min,n)
def Size(heap):
    return len(heap)

def Add(heap,x):
    heap.append(x)

    n=len(heap)

    i=n-1

    while(i>0 and heap[(i-1)//2]>heap[i]):
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

def Peek(heap):
    return heap[0]


def klargest(arr,k):

    heap=Heap()

    for i in range(k):
        heap.append(arr[i])

    makeheap(heap)

    for i in range(k,len(arr)):
        if arr[i]>Peek(heap):
            x=extractmin(heap)
            Add(heap,arr[i])
    while(Size(heap)>0):
        x=extractmin(heap)
        print(x,end=' ')
    

arr=[2,10,5,17,7,18,6,4]

klargest(arr,3)







