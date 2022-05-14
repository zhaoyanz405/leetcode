"""
给定二叉搜索树（BST）的根节点root和一个整数值val。

你需要在 BST 中找到节点值等于val的节点。 返回以该节点为根的子树。 如果节点不存在，则返回null。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return

        if root.val == val:
            return root

        elif root.val > val:
            return self.searchBST(root.left, val)
        elif root.val < val:
            return self.searchBST(root.right, val)
