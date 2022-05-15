"""
给定一棵二叉树的根节点rootTreeNode对象的数组（列表）nodes，返回nodes中所有节点的最近公共祖先（LCA）。数组（列表）中所有节点都存在于该二叉树中，且二叉树中所有节点的值都是互不相同的。

我们扩展二叉树的最近公共祖先节点在维基百科上的定义：“对于任意合理的 i 值，n个节点p1、p2、...、pn在二叉树T中的最近公共祖先节点是后代中包含所有节点pi的最深节点（我们允许一个节点是其自身的后代）”。一个节点 x的后代节点是节点x 到某一叶节点间的路径中的节点 y。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iv
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def __init__(self):
        self.nodes = None

    def lowestCommonAncestor(self, root: TreeNode, nodes: list) -> TreeNode:
        self.nodes = [n.val for n in nodes]
        return self.find(root)

    def find(self, root):
        if not root:
            return

        if root.val in self.nodes:
            return root

        left = self.find(root.left)
        right = self.find(root.right)

        if left and right:
            return root

        return left if left else right
