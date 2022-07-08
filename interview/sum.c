#include <stdio.h>
#include <stdlib.h>

int main() {
    const int N = 10;
    int a[N];
    a[0] = 0;
    a[1] = 1;

    for (size_t i = 2; i < N; i++)
    {
        a[i] = a[i-1] + a[i-2];
    }

    for (size_t i = 0; i < N; i++)
    {
        printf("%d\n", a[i]);
    }

    int b[] = {1,2,4,7,11,16,22};
    int n = sizeof(b) / sizeof(b[0]);
    int sum = 0;
    for (size_t i = 0; i < n; i++)
    {
        sum += b[i];
    }
    printf("%d\n", sum);

    return 0;
}
