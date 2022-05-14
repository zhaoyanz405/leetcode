"""
给定一个二叉搜索树的根节点 root ，和一个整数 k ，请你设计一个算法查找其中第 k 个最小元素（从 1 开始计数）。
"""
from binarytree.treenode import TreeNode, create_tree


class Solution:
    def __init__(self):
        self.count = 0
        self.result = 0

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.inorder_traverse(root, k)
        return self.result

    def inorder_traverse(self, root, k):
        if not root:
            return

        self.inorder_traverse(root.left, k)

        self.count += 1
        if self.count == k:
            self.result = root
            return

        self.inorder_traverse(root.right, k)


if __name__ == '__main__':
    s = Solution()
    print(s.inorder_traverse(create_tree([3, 1, 4, None, 2]), k=1))
