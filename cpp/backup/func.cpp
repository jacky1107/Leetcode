#include <stdio.h>
#include <stdlib.h>

int* add(int* a, int* b) {
    int *c = (int*)malloc(sizeof(int));
    *c = *a + *b;
    return c;
}

int sub(int a, int b) {
    return a - b;
}

void print_char(char *c) {
    printf("%s\n", c);
}

void func1() {
    printf("sdfsdf\n");
}

void func2(void (*func)()) {
    func();
}

void bubble_sort(int *array, int length, int (*compare)(int, int)) {
    int temp;
    for (size_t i = 0; i < length; i++)
    {
        for (size_t j = i; j < length; j++)
        {
            if (compare(array[i], array[j]) > 0) {
                temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
    }

    for (size_t i = 0; i < length; i++)
    {
        printf("%d\n", array[i]);
    }
}

int compare(int a, int b) {
    int temp = -1;
    if (a > b) return temp;
    else return -temp;
}

int main() {
    int a = 2, b = 4;
    int *ptr = add(&a, &b);
    printf("%d\n", *ptr);

    int (*func)(int, int);
    func = sub;
    printf("%d\n", func(a, b));

    char *c = (char*)"SD";
    void (*prt)(char *);
    prt = print_char;
    prt(c);
    func2(func1);

    int array[] = {3,4,1,5,3,2,7};
    int length = sizeof(array) / sizeof(*array);
    bubble_sort(array, length, compare);

    return 0;
}