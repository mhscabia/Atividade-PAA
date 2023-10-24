import random
import time
import matplotlib.pyplot as plt

def pesquisaBinariaNaoRecursiva(lista, item):
    lista_ordenada = sorted(lista)
    primeiro = 0
    ultimo = len(lista_ordenada) - 1
    while primeiro <= ultimo:
        meio = (primeiro + ultimo) // 2
        if lista_ordenada[meio] == item:
            return meio
        else:
            if item < lista_ordenada[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return None

# Generate random arrays of integers
sizes = [1000, 10000, 100000]
times = []
for size in sizes:
    data = [random.randint(0, 100) for _ in range(size)]

    # Sort the array and measure the elapsed time
    start_time = time.time()
    retorno = pesquisaBinariaNaoRecursiva(data, 50)
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