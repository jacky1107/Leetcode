#include <stdio.h>
#include <string.h>

void func(int (*A)[3]) {
}

int main() {
    int B[2][3] = {{1,2,3}, {4,5,6}};
    int (*p)[3] = B;
    printf("%d\n", *(*(B+1)+1));
    printf("%d\n", B[0][0]);

    func(B);
    return 0;
}