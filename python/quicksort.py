import random
import time
import matplotlib.pyplot as plt

# function to partition the array on the basis of pivot element
def partition(array, low, high):
    i = (low - 1)
    pivot = array[high]
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
 
            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])
 
    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])
 
    # Return the position from where partition is done
    return i + 1
 
# function to perform quicksort
def quickSort(array):
    # Create an empty stack
    stack = []
 
    # Push initial values of low and high to stack
    stack.append((0, len(array) - 1))
 
    # Loop until stack is empty
    while stack:
 
        # Pop low and high from stack
        low, high = stack.pop()
 
        # Set pivot element at its correct position in sorted array
        pi = partition(array, low, high)
 
        # If there are elements on left side of pivot,
        # then push left side to stack
        if pi - 1 > low:
            stack.append((low, pi - 1))
 
        # If there are elements on right side of pivot,
        # then push right side to stack
        if pi + 1 < high:
            stack.append((pi + 1, high))

# Generate random arrays of integers
sizes = [1000, 5000, 10000, 20000, 50000, 75000, 100000]
times = []
for size in sizes:
    data = [random.randint(0, 100) for _ in range(size)]

    # Sort the array and measure the elapsed time
    start_time = time.time()
    quickSort(data)
    end_time = time.time()

    # Append the elapsed time to the list of times
    times.append(end_time - start_time)
    print("Tempo decorrido no tamanho",size,":", round(end_time - start_time, 3), "segundos")

# Plot the graph
plt.plot(sizes, times, 'o-')
plt.xlabel('Array size')
plt.ylabel('Time elapsed (s)')
plt.show()