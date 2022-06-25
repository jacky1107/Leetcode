#include <iostream>
#include <stdio.h>
#include <cmath>
#include <cstring>

void reverse_string(char *s){
    size_t length = strlen(s);
    char temp;
    for (size_t i = 0; i < length/2; i++)
    {
        temp = s[length-1-i];
        s[length-1-i] = s[i];
        s[i] = temp;
    }
}

int main() {
    char s[10];
    std::cin.getline(s, 10);
    reverse_string(s);
    for (size_t i = 0; i < strlen(s); i++)
    {
        printf("%c\n", s[i]);
    }

    return 0;
}