"""
给定一棵二叉树的根节点 root，返回给定节点 p 和 q 的最近公共祖先（LCA）节点。如果 p 或 q 之一 不存在 于该二叉树中，返回 null。树中的每个节点值都是互不相同的。

根据维基百科中对最近公共祖先节点的定义：“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是 后代节点 中既包括 p 又包括 q 的最深节点（我们允许 一个节点为自身的一个后代节点 ）”。一个节点 x 的 后代节点 是节点 x 到某一叶节点间的路径中的节点 y。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def __init__(self):
        self.found_p = None
        self.found_q = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = self.find(root, p, q)
        if self.found_q or self.found_q:
            return res

    def find(self, root, p, q):
        if not root:
            return

        left = self.find(root.left, p, q)
        right = self.find(root.right, p, q)

        if root == p or root == q:
            if root == p:
                self.found_p = True
            if root == q:
                self.found_q = True
            return root

        if left and right:
            return root

        if not left and not right:
            return

        return left if left else right
