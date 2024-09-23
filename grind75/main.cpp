#include <stdio.h>
#include <iostream>

#include <map>
#include <stack>
#include <vector>
#include <string.h>
#include <unordered_map>


struct ListNode {
    int val;
    ListNode *next;

    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *node) : val(x), next(node) {}
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
        if (list1) temp->next = list1;
        if (list2) temp->next = list2;
        return dummy->next;
    }
};

int main() {
    ListNode *n13 = new ListNode(4);
    ListNode *n12 = new ListNode(2, n13);
    ListNode *n11 = new ListNode(1, n12);

    ListNode *n23 = new ListNode(4);
    ListNode *n22 = new ListNode(3, n23);
    ListNode *n21 = new ListNode(1, n22);

    Solution sol;
    n11 = sol.mergeTwoLists(n11, n21);

    while (n11)
    {
        std::cout << n11->val << std::endl;
        n11 = n11->next;
    }
    

    return 0;
}