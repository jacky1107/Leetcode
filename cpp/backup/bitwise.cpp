#include <iostream>
#include <stdio.h>
#include <string.h>

int main(void) {
    int N = 1022;
    printf("%d %d\n", N & 15, N % 16);
    printf("%d %d\n", N >> 4, N / 16);
    printf("%d %d\n", N << 2, N * 4);

    int a = 3, b = 5;
    a = a ^ b;
    b = b ^ a;
    a = a ^ b;
    printf("%d %d\n", a, b);

    return 0;
}
