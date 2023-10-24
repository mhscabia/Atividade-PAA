import random
import matplotlib.pyplot as plt
import time

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Generate random arrays of integers
sizes = [1000, 10000, 100000]
times = []
for size in sizes:
    data = [random.randint(0, 100) for _ in range(size)]

    # Sort the array and measure the elapsed time
    start_time = time.time()
    bubbleSort(data)
    end_time = time.time()

    # Append the elapsed time to the list of times
    times.append(end_time - start_time)
    print("Tempo decorrido no tamanho",size,":", round(end_time - start_time, 3), "segundos")

# Plot the graph
plt.plot(sizes, times, 'o-')
plt.xlabel('Array size')
plt.ylabel('Time elapsed (s)')
plt.show()