#include <iostream>
#include <string>
#include <vector>
using namespace std;


    // string temp = "";
    // for (size_t i = 0; i < str.length(); i++)
    // {
    //     char s = str[i];
    //     if (s == '[' || s == ' ' || s == ']') continue;
    //     else if (s != ',') temp += s;
    //     else {
    //         arr.push_back(stoi(temp));
    //         temp = "";
    //     }
    // }
    // arr.push_back(stoi(temp));

int get_elements_int(string str, int *index) {
    string temp = "";
    while (*index < str.length())
    {
        char s = str[*index];
        if (isdigit(s)) temp += s;
        else if (s == ',') return stoi(temp);
        *index += 1;
    }
}

string ArrayMatching(string strArr[], int arrLength) {
    int min_length = min(strArr[0].size(), strArr[1].size());
    int i = 0, j = 0;
    int *p = &i, *q = &j;
    string t1, t2;
    while (i < min_length || j < min_length)
    {
        int a1 = get_elements_int(strArr[0], p);
        int a2 = get_elements_int(strArr[1], q);
        cout << a1 + a2 << *p << endl;

        if (strArr[0][*p] == ']') {
            t2 = strArr[1].substr(j, strArr[1].length());
            break;
        } else if (strArr[1][*q]  == ']') {
            t1 = strArr[0].substr(i, strArr[0].length());
            break;
        }
        *p += 1;
        *q += 1;
    }
    cout << strArr[0] << t2 << endl;

    // code goes here
    return strArr[0];
}



int main(void) { 
    // keep this function call here
    string A[] = {"[5, 2, 3]", "[2, 2, 3, 10, 6]"}; //coderbyteInternalStdinFunction(stdin);
    int arrLength = sizeof(A) / sizeof(*A);
    ArrayMatching(A, arrLength);
    return 0;
}