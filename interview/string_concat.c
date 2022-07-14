#include <stdio.h>
#include <string.h> // For strcat function

int main(void) {
    char str1[60] = "123";
    char str2[] = "234";

    strcat(str1, str2);
    printf("%s\n", str1);
    
    return 0;
}