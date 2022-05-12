"""
给定两个整数数组 inorder 和 postorder ，其中 inorder 是二叉树的中序遍历， postorder 是同一棵树的后序遍历，请你构造并返回这颗 二叉树 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-inorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def buildTree(self, inorder: list, postorder: list) -> TreeNode:
        if not inorder or not postorder:
            return

        root = postorder[-1]

        inorder_map = {n: i for i, n in enumerate(inorder)}
        rootidx = inorder_map[root]

        left_inorder = inorder[:rootidx]
        right_inorder = inorder[rootidx + 1:]

        left_postorder = postorder[:rootidx]
        right_postorder = postorder[rootidx: len(right_inorder) + rootidx]

        node = TreeNode(root)
        node.left = self.buildTree(left_inorder, left_postorder)
        node.right = self.buildTree(right_inorder, right_postorder)

        return node


if __name__ == '__main__':
    s = Solution()
    s.buildTree(inorder=[1, 2], postorder=[2, 1])
