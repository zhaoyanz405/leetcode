"""
给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。

有效 二叉搜索树定义如下：

节点的左子树只包含 小于 当前节点的数。
节点的右子树只包含 大于 当前节点的数。
所有左子树和右子树自身必须也是二叉搜索树。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/validate-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.is_valid(root)

    def is_valid(self, root, node_min=None, node_max=None):
        """限定node_max.val > root.val > node_min.val"""
        if not root:
            return True

        if node_min and root.val <= node_min.val:
            return False

        if node_max and root.val >= node_max.val:
            return False

        return self.is_valid(root.left, node_min, root) and self.is_valid(root.right, root, node_max)
