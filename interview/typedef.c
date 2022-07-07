#include <stdio.h>
void(*(*papf)[3])(char *);
typedef void(*pf)(char *);

int main(void) {
    pf(*papf)[3];
    return 0;
}