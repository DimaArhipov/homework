from random import randrange
import time
from datetime import datetime

def merge_sort(a):
    if len(a)>1:
        mid = len(a)//2
        lefthalf = a[:mid]
        righthalf = a[mid:]

        merge_sort(lefthalf)
        merge_sort(righthalf)

        i=0
        j=0
        k=0
        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i]<righthalf[j]:
                a[k]=lefthalf[i]
                i=i+1
            else:
                a[k]=righthalf[j]
                j=j+1
            k=k+1

        while i<len(lefthalf):
            a[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j<len(righthalf):
            a[k]=righthalf[j]
            j=j+1
            k=k+1
    return a

def heapsort(a):                                 
    def down_heap(a, k, n):                            
        parent = a[k]                                  

        while 2*k+1 < n:                                 
            child = 2*k+1                                
            if child+1 < n and a[child] < a[child+1]:
                child += 1                               
            if parent >= a[child]:                     
                break                                    
            a[k] = a[child]                          
            k = child                                    
        a[k] = parent                                  

    size = len(a)                                      

    for i in range(size//2-1, -1, -1):                    
        down_heap(a, i, size)                          

    for i in range(size-1, 0, -1):                       
        a[0], a[i] = a[i], a[0]                  
        down_heap(a, 0, i) 
    return a

def quicksort(array):
    qsort(array, 0, len(array) - 1)
    return a

def qsort(array, start, stop):
    if stop - start > 0:
        pivot, left, right = array[start], start, stop
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
        qsort(array, start, right)
        qsort(array, left, stop)

a = [65, 55, 96, 49, 45, 95, 5, 21]
print(a)
from datetime import datetime
start_time = datetime.now()
print(merge_sort(a))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
a = [65, 55, 96, 49, 45, 95, 5, 21]
print(a)
from datetime import datetime
start_time = datetime.now()
print(heapsort(a))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
a = [65, 55, 96, 49, 45, 95, 5, 21]
print(a)
from datetime import datetime
start_time = datetime.now()
print(quicksort(a))
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
