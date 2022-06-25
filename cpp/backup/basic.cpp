#include <iostream>
#include <stdio.h>
#include <cmath>

#define MAX(a, b) (a > b)? a : b
#define SECONDS_PER_YEAR 60 * 60 * 24 * 365UL
#define square(a) (a * a)

int add(int &x) {
    x = x + 1;
}

int main(void) {
    int x = 10, z = 3;
    int *y;
    *y = 5;
    z = z + 1;
    x = x + *y;
    printf("x = %d\n", x); // 15
    printf("y = %d\n", *y); // 5
    printf("z = %d\n", z); // 4

    y = &x;
    printf("y = %d\n", *y); // 15
    printf("MAX: %d\n", MAX(x, z)); // x = 15

    unsigned long int s = SECONDS_PER_YEAR;
    printf("Seconds per year: %lu\n", s); // 31536000
    printf("Square of a: %d\n", square(x)); // 225

    int a[5] ={1,3,5,7,9};
    int *p = (int *)(&a + 1);
    std::cout << *(a+1) << std::endl;
    std::cout << *(p-1) << std::endl;
    std::cout << std::endl;

    int c = 5;
    std::cout << c << std::endl;
    add(c);
    std::cout << c << std::endl;
    std::cout << std::endl;

    long long int aa = INT64_MAX; // 8 * 8
    long int bb = INT32_MAX; // 4 * 8
    int cc = INT32_MAX; // 4 * 8
    short int dd = INT16_MAX; // 4 * 8

    printf("%lld %d\n", aa, sizeof(aa));
    printf("%ld %d\n", bb, sizeof(bb));
    printf("%d %d\n", cc, sizeof(cc));
    printf("%d %d\n", dd, sizeof(dd));

    return 0;
}