import random
import time
import matplotlib.pyplot as plt


def pesquisaBinariaRecursiva(lista, item):
    lista_ordenada = sorted(lista)
    if len(lista_ordenada) == 0:
        return False
    else:
        meio = len(lista_ordenada) // 2
        if lista_ordenada[meio] == item:
            return True
        else:
            if item < lista_ordenada[meio]:
                return pesquisaBinariaRecursiva(lista_ordenada[:meio], item)
            else:
                return pesquisaBinariaRecursiva(lista_ordenada[meio + 1:], item)
            
# Generate random arrays of integers
sizes = [1000, 5000, 10000, 20000, 50000, 75000, 100000]
times = []
for size in sizes:
    data = [random.randint(0, 100) for _ in range(size)]

    # Sort the array and measure the elapsed time
    start_time = time.time()
    retorno = pesquisaBinariaRecursiva(data, 50)
    end_time = time.time()
    print(retorno)

    # Append the elapsed time to the list of times
    times.append(end_time - start_time)
    print("Tempo decorrido no tamanho",size,":", round(end_time - start_time, 3), "segundos")

# Plot the graph
plt.plot(sizes, times, 'o-')
plt.xlabel('Array size')
plt.ylabel('Time elapsed (s)')
plt.show()