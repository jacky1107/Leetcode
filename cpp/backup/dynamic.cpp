#include <stdio.h>
#include <stdlib.h>

int main() {
    int *p;
    p = (int*)malloc(sizeof(int));
    *p = 20;
    printf("%d\n", *p);
    free(p); // for release the memory from the heap
    p = (int*)malloc(sizeof(int));
    *p = 10;
    printf("%d\n", *p);

    int *q = new int;
    int *k = new int[20];
    *q = 5;
    delete q;
    delete[] k;

    return 0;
}