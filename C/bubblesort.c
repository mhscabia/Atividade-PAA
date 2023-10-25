#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void bubbleSort(int arr[], int n) {
    int i, j, temp;
    for (i = 0; i < n - 1; i++) {
        for (j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                /* Troca os elementos adjacentes se o primeiro for maior que o segundo */
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

int main() {
    int sizes[] = {1000, 5000, 10000, 20000, 50000, 75000, 100000}; /* Tamanhos dos arrays a serem ordenados */
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]); /* Número de tamanhos */
    srand(time(NULL)); /* Inicializa o gerador de números aleatórios com o tempo atual */

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        int arr[n];
        for (int j = 0; j < n; j++) {
            arr[j] = rand() % 101; /* Gera um número aleatório entre 0 e 100 */
        }

        clock_t inicio = clock(); /* Marca o tempo de início da ordenação */
        bubbleSort(arr, n);
        clock_t fim = clock(); /* Marca o tempo de fim da ordenação */

        double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC; /* Calcula o tempo de execução em segundos */
        printf("Tempo de execucao do tamanho %d foi: %.4f segundos\n", n, tempo);
    }

    return 0;
}