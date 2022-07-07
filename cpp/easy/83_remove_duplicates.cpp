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
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode *prev = head;
        ListNode *curr = head->next;
        while (curr)
        {
            if (prev->val == curr->val) {
                prev->next = curr->next;
            } else {
                prev = curr;
            }
            curr = curr->next;
        }
        return head;
    }
};

int main() {
    ListNode *s3 = new ListNode(2);
    ListNode *s2 = new ListNode(1, s3);
    ListNode *s1 = new ListNode(1, s2);

    Solution sol;
    ListNode *result = sol.deleteDuplicates(s1);

    printf("\n");
    while (result)
    {
        printf("%d\n", result->val);
        result = result->next;
    }
    return 0;
}