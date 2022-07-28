#include <iostream>
#include <vector>
#include <string.h>
#include <ctype.h>
#include <cctype>

using namespace std;

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};


void print(TreeNode *root) {
    if (root != nullptr)
    {
        cout << root->val << endl;
        print(root->left);
        print(root->right);
    }
}

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if (root != nullptr) {
            swap(root->left, root->right);
            invertTree(root->left);
            invertTree(root->right);
        }
        return root;
    }
};

int main(void) {
    TreeNode *node = new TreeNode(4);
    node->left = new TreeNode(2);
    node->left->left = new TreeNode(1);
    node->left->right = new TreeNode(3);

    node->right = new TreeNode(7);
    node->right->left = new TreeNode(6);
    node->right->right = new TreeNode(9);

    Solution sol;
    TreeNode *res = sol.invertTree(node);
    print(res);
}
