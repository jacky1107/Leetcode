#include <stdio.h>
#include <stdbool.h> // # for type <bool> 
#include <windows.h>

bool detectCapitalUse(char* word){
    int count1 = 0;
    int count2 = 0;
    for (size_t i = 0; i < strlen(word); i++)
    {
        if ('A' <= word[i] && word[i] <= 'Z') count1++;
        else count2++;
    }
    if (count1 == strlen(word) || count2 == strlen(word)) return true;
    if (count1 == 1 && ('A' <= word[0] && word[0] <= 'Z')) return true;
    else return false;
}

int main(void) {
    char str[50]; // size of char string  
    printf("Enter the string: ");  
    scanf("%s", str);

    bool b = detectCapitalUse(str);
    printf("%d\n", b);
    return 0;
}