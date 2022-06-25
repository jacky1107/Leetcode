#include <iostream>
#include <stdio.h>
#include <vector>

const int Max = 10000;

void print_array(std::vector<int> &array) {
    for (size_t i = 0; i < array.size(); i++)
    {
        printf("%d ", array[i]);
    }
    printf("\n");
}

void merge(std::vector<int> &array, int start, int mid, int end) {
    std::vector<int> left_array(array.begin()+start, array.begin()+mid+1);
    std::vector<int> right_array(array.begin()+mid+1, array.begin()+end+1);

    left_array.insert(left_array.end(), Max);
    right_array.insert(right_array.end(), Max);

    int l = 0, r = 0;
    for (size_t i = start; i <= end; i++)
    {
        if (left_array[l] <= right_array[r])
        {
            array[i] = left_array[l];
            l++;
        } else {
            array[i] = right_array[r];
            r++;
        }
    }
}

void merge_sorted(std::vector<int> &array, int start, int end) {
    if (start < end) {
        int mid = (start + end) / 2;
        merge_sorted(array, start, mid);
        merge_sorted(array, mid+1, end);
        merge(array, start, mid, end);
    }
}

int main() {

    int arr[] = {4,5,3,1,2,3,6,4};
    std::vector<int> array(arr, arr+sizeof(arr)/sizeof(int));
    print_array(array);
    merge_sorted(array, 0, array.size() - 1);
    print_array(array);

    return 0;
}