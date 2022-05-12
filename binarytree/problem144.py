"""
给你二叉树的根节点 root ，返回它节点值的 前序 遍历。
"""
from binarytree.treenode import TreeNode, create_tree


class Solution:
    res = []

    def preorderTraversal(self, root: TreeNode) -> list:
        if root is None:
            return []

        self.res.append(root.val)

        self.preorderTraversal(root.left)
        self.preorderTraversal(root.right)

        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.preorderTraversal(create_tree([0, 1, 2, 3, 4, 5, 6], 0)))
