#include <stdio.h>

int add(int a, int b) {
    return a + b;
}

int main(void) {
    int (*op)(int a, int b);
    op = add;
    printf("%d\n", op(2, 5));
    return 0;
}