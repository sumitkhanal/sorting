import random
from time import time_ns
from insertionsort import insertionsort
from mergesort import mergesort
import matplotlib.pyplot as plt 
 
def run():
    numbers = range(10000)
    datas = []
    times = []
 
    sizes = [10, 100, 500, 1000, 5000, 10000, 20000, 30000]
 
    for s in sizes:
        datas.append(random.choices(numbers, k=int(s)))
 
    print('Insertion Sort\n')
    for data in datas:  
        startTime = time_ns()
        insertionsort(data)
        endTime = time_ns()
 
        executionTime = endTime - startTime
 
        print( len(data), 'Datas ->', executionTime, 'nanoseconds')
        times.append(executionTime / 1000000000)
    plotSort( sizes, times, 'Insertion Sort')

    times.clear()

    print('\n\nMerge Sort\n')
    for data in datas:
        startTime = time_ns()
        mergesort(data)
        endTime = time_ns()
 
        executionTime = endTime - startTime
 
        print( len(data), 'Datas ->', executionTime, 'nanoseconds')
        times.append(executionTime / 1000000000)
    plotSort( sizes, times, 'Merge Sort')
 
def plotSort(x, y, sortType):
    plt.plot(x, y) 

    plt.xlabel('Data Size') 
    plt.ylabel('Time in Seconds') 
    
    plt.title(sortType) 
    plt.show() 


if __name__ == '__main__':
    run()