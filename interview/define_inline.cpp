#include <stdio.h>

#define SUM(x, y) x + y

int var = 100;
int add(int x, int y) {
    return x + y;
}

inline int sub(int a, int b) {
    return a - b;
}

int main(void) {
    printf("%d\n", SUM(2, 5) * 10);

    int (*op)(int a, int b);
    op = add;
    printf("%d\n", op(2, 5));
    printf("%d\n", sub(5, 2));

    extern int var;
    printf("%d\n", var);
    return 0;
}