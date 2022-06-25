#include <stdio.h>
#include <string.h>

int sum_of_array(int *a, int length) {
    int sum = 0;
    for (size_t i = 0; i < length; i++)
    {
        sum += a[i];
    }
    return sum;
}

void print_char(char *c) {
    // 1
    int i = 0;
    while (*(c+i) != '\0')
    {
        printf("%c", c[i]);
        i++;
    }
    printf("\n");

    // 2
    while (*c != '\0')
    {
        printf("%c", *c);
        c++;
    }
    printf("\n");
}

int main() {
    char c[] = "Jacky Wang";
    char *c2 = c;
    int len = strlen(c);
    printf("%d\n", sizeof(c)); // \0
    printf("%d\n", len);
    printf("%c\n", *(c+2));
    printf("%c\n", *(c2+3));
    print_char(c);

    int a[] = {1, 2, 3, 4, 5};
    int length = sizeof(a) / sizeof(a[0]);
    int sum = sum_of_array(a, length);
    printf("%d\n", sum);
    return 0;
}