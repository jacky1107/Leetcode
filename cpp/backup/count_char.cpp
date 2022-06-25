#include <iostream>
#include <stdio.h>
#include <string.h>

int main(void) {
    const char* a = "hello";
    int i = 0, count = 0;
    while (a[i] != '\0')
    {
        i++;
    }
    printf("%d\n", i);
    return 0;
}
