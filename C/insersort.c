#include <stdio.h>
#include <time.h>
#include <stdlib.h>

void insertionSort(int arr[], int n) {
    int i, key, j;
    for (i = 1; i < n; i++) {
        key = arr[i];
        j = i - 1;

        /* Move os elementos do arr[0..i-1], que são maiores que a chave, para uma posição à frente de sua posição atual */
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j = j - 1;
        }
        arr[j + 1] = key;
    }
}

int main() {
    int n = 1000;
    int arr[n];
    srand(time(NULL)); /* Inicializa o gerador de números aleatórios com o tempo atual */
    for (int i = 0; i < n; i++) {
        arr[i] = rand() % 101; /* Gera um número aleatório entre 0 e 100 */
    }

    clock_t inicio = clock(); /* Marca o tempo de início da ordenação */
    insertionSort(arr, n);
    clock_t fim = clock(); /* Marca o tempo de fim da ordenação */

    double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC; /* Calcula o tempo de execução em segundos */
    printf("Tempo de execucao: %.2f segundos\n", tempo);
    return 0;
}