#include <stdio.h>
#include <windows.h>

void reverse_string(char *s) {
    for (size_t i = 0; i < strlen(s) / 2; i++)
    {
        char temp = s[i];
        s[i] = s[strlen(s) - i - 1];
        s[strlen(s) - i - 1] = temp;
    }
}

void print_string(char *s) {
    for (size_t i = 0; i < strlen(s); i++)
    {
        printf("%c\n", s[i]);
    }
}

int main(void) {
    char str[50]; // size of char string  
    printf("Enter the string: ");  
    scanf("%s", str);

    reverse_string(str);
    print_string(str);
    return 0;
}