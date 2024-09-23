#include <iostream>
#include <stdio.h>

struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
};
 
class Solution {
public:
	int goodNodes(TreeNode* root) {
		int count = 0;
		int maxValue = -10000;
		count = recursive(root, maxValue, count);
		return count;
	}

	int recursive(TreeNode* root, int value, int count) {
		if (root != nullptr) {
			if (root->val >= value) {
				value = root->val;
				count++;
			}
			count = recursive(root->left, value, count);
			count = recursive(root->right, value, count);
		}
		return count;
	}
};

int main() {
	TreeNode *node = new TreeNode(-1);

    node->right = new TreeNode(-2);
    node->right->right = new TreeNode(-2);
	
    node->right->right->right = new TreeNode(-2);
    node->right->right->right->left = new TreeNode(-4);

    node->right->right->right->right = new TreeNode(-3);
    node->right->right->right->right->left = new TreeNode(3);
    node->right->right->right->right->right = new TreeNode(-3);

	Solution sol;
	int res = sol.goodNodes(node);
    printf("%d\n", res);
	return 0;
}