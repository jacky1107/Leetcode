#include<stdio.h>
#define FUN(X) (#X[1])

int main() {
    printf("%d\n", FUN(cd));
    return 0;
}
