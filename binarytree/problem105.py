"""
给定两个整数数组preorder 和 inorder，其中preorder 是二叉树的先序遍历， inorder是同一棵树的中序遍历，请构造二叉树并返回其根节点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def __init__(self):
        self.inorder_map = {}

    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        if not preorder or not inorder:
            return

        root = preorder[0]

        self.inorder_map = {n: i for i, n in enumerate(inorder)}

        root_idx_inoder = self.inorder_map[root]
        left_inorder = inorder[:root_idx_inoder]
        right_inorder = inorder[root_idx_inoder + 1:]

        left_preorder = preorder[1: len(left_inorder) + 1]
        right_preorder = preorder[len(left_inorder) + 1:]

        node = TreeNode(root)
        node.left = self.buildTree(left_preorder, left_inorder)
        node.right = self.buildTree(right_preorder, right_inorder)

        return node


if __name__ == '__main__':
    s = Solution()
    s.buildTree(preorder=[1, 2], inorder=[1, 2])
