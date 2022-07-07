#include <stdio.h>

struct S
{
    char a[32];
    int b[4];
    long int c;
    unsigned int d;
    unsigned long int e;
    double f;
};

union U
{
    char a[32];
    int b[4];
    long int c;
    unsigned int d;
    unsigned long int e;
    double f;
};


int main(void) {
    
    struct S s1;
    printf("%d\n", sizeof(s1));
    printf("%d\n", sizeof(s1.a));
    printf("%d\n", sizeof(s1.b));
    printf("%d\n", sizeof(s1.c));
    printf("%d\n", sizeof(s1.d));
    printf("%d\n", sizeof(s1.e));
    printf("%d\n", sizeof(s1.f));

    union U u1;
    printf("%d\n", sizeof(u1));
    printf("%d\n", sizeof(u1.a));
    printf("%d\n", sizeof(u1.b));
    printf("%d\n", sizeof(u1.c));
    printf("%d\n", sizeof(u1.d));
    printf("%d\n", sizeof(u1.e));
    printf("%d\n", sizeof(u1.f));

    return 0;
}