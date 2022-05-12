"""
给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。
"""
from binarytree.treenode import TreeNode


class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
