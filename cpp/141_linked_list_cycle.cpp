#include <stdio.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <unordered_map>
using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
    bool hasCycle(ListNode *head) {
        unordered_map<ListNode*, bool> visited;
        while(head) {
            visited[head] = true;
            if (visited.count(head->next)) {
                return true;
            } 
            head = head->next;
        }
        return 0;
    }
};

int main() {
    ListNode *s = new ListNode(3);
    s->next = new ListNode(2);
    s->next->next = new ListNode(0);
    s->next->next->next = new ListNode(4);
    s->next->next->next = s->next;

    Solution sol;
    int result = sol.hasCycle(s);
    printf("%d\n", result);
    return 0;
}