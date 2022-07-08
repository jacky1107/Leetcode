#include <stdio.h>
#include <windows.h>

int main(void) {
    printf("size of BYTE = %d\n \
        size of float = %d\n \
        size of unsigned int = %d\n \
        size of unsigned long = %d\n \
        size of int = %d\n \
        size of double = %d\n \
        size of unsigned char = %d\n \
        size of char = %d\n"
        ,sizeof(BYTE)          // 1
        ,sizeof(float)         // 4
        ,sizeof(unsigned int)  // 4
        ,sizeof(unsigned long)  // 4
        ,sizeof(int)           // 4
        ,sizeof(double)        // 8
        ,sizeof(unsigned char) // 1
        ,sizeof(char));        // 1

    return 0;
}