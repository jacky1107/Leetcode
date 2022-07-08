#include <stdio.h>
#include <windows.h>

int main(void) {
    int x = 10, z = 3;
    int *y;
    *y = 5;
    z = z + 1;
    x = x + *y;
    printf("x = %d\n", x);   // 15
    printf("*y = %d\n", *y); // 5
    printf("z = %d\n", z);   // 4

    y = &x;                  
    printf("y = %d\n", *y);  // 15

    // &z is lvalue, so this cannot access the value.
    // lvalue required as left operand of assignment
    // &z = y;
    printf("z = %d\n", z);
    return 0;
}