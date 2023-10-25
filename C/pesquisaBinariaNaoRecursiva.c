#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int binarySearch(int arr[], int n, int x) {
    int left = 0, right = n - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == x) {
            return mid;
        } else if (arr[mid] < x) {
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }
    return -1;
}

int cmpfunc(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

int main() {
    int sizes[] = {100000}; /* Tamanhos dos arrays a serem pesquisados */
    int num_sizes = sizeof(sizes) / sizeof(sizes[0]); /* Número de tamanhos */
    srand(time(NULL)); /* Inicializa o gerador de números aleatórios com o tempo atual */

    for (int i = 0; i < num_sizes; i++) {
        int n = sizes[i];
        int arr[n];
        for (int j = 0; j < n; j++) {
            arr[j] = rand() % 1001; /* Gera um número aleatório entre 0 e 100 */
        }
        int x = rand() % 1001; /* Gera um número aleatório para ser pesquisado */

        qsort(arr, n, sizeof(int), cmpfunc); /* Ordena o array em ordem crescente */

        clock_t inicio = clock(); /* Marca o tempo de início da pesquisa */
        int pos = binarySearch(arr, n, x);
        clock_t fim = clock(); /* Marca o tempo de fim da pesquisa */

        double tempo = (double)(fim - inicio) / CLOCKS_PER_SEC; /* Calcula o tempo de execução em segundos */
        if (pos == -1) {
            printf("O elemento %d nao foi encontrado no array de tamanho %d em %.4f segundos\n", x, n, tempo);
        } else {
            printf("O elemento %d foi encontrado na posicao %d do array de tamanho %d em %.4f segundos\n", x, pos, n, tempo);
        }
    }

    return 0;
}