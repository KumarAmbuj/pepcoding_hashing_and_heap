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
    if r<n and heap[r].val < heap[min].val:
        min=r

    if min !=i:
        heap[i],heap[min]=heap[min],heap[i]
        heapify(heap,min,n)


def mergeksorted(arr)