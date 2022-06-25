#include <iostream>
#include <string>
using namespace std;

string LRUCache(string strArr[], int arrLength) {
    for (size_t i = 0; i < arrLength; i++)
    {
        printf("%s\n", strArr[i].c_str());
    }
    
    // code goes here
    return strArr[0];
}

int main(void) { 
    
    // keep this function call here
    string A[] = {"A", "B", "A", "C", "A", "B"}; //coderbyteInternalStdinFunction(stdin);
    printf("%s\n", (A+1)->c_str());

    int arrLength = sizeof(A) / sizeof(*A);
    cout << LRUCache(A, arrLength);
    return 0;
    
}