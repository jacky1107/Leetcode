#include <stdio.h>
#include <string.h>
#include <vector>
#include <unordered_map>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        ListNode *dummy = new ListNode(0);
        ListNode *temp = dummy;
        while (list1 && list2)
        {
            if (list1->val > list2->val) {
                temp->next = list2;
                list2 = list2->next;
            } else {
                temp->next = list1;
                list1 = list1->next;
            }
            temp = temp->next;
        }
        if(list1) temp->next = list1;
        if(list2) temp->next = list2;
        return dummy->next;
    }
};

int main() {
    ListNode *n3 = new ListNode(4);
    ListNode *n2 = new ListNode(2, n3);
    ListNode *n1 = new ListNode(1, n2);

    ListNode *s3 = new ListNode(4);
    ListNode *s2 = new ListNode(3, s3);
    ListNode *s1 = new ListNode(1, s2);

    Solution sol;
    ListNode *result = sol.mergeTwoLists(n1, s1);

    while (result)
    {
        printf("%d\n", result->val);
        result = result->next;
    }

    return 0;
}