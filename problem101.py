"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。
"""

from treenode import TreeNode, create_tree


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        # 直接从左右子树开始比较
        return self._is_sym(root.left, root.right)

    def _is_sym(self, node1, node2):
        if node1 == node2:
            return True

        if node1 is None or node2 is None:
            return False

        if node1.val == node2.val:
            left_sym = self._is_sym(node1.left, node2.right)
            right_sym = self._is_sym(node1.right, node2.left)
            if left_sym and right_sym:
                return True
            else:
                return False
        else:
            return False


if __name__ == '__main__':
    node = create_tree([1, 2, 2, None, 3, None, 3])

    s = Solution()
    print(s.isSymmetric(node))
