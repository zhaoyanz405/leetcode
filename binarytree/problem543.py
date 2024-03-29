"""
给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

示例 :
给定二叉树

          1
         / \
        2   3
       / \
      4   5
返回3, 它的长度是路径 [4,2,1,3] 或者[5,2,1,3]。


注意：两结点之间的路径长度是以它们之间边的数目表示。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/diameter-of-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    diameter = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        # diameter = maxdepth(left) + maxdepth(right)
        if not root:
            return 0

        self.maxdepth(root)
        return self.diameter

    def maxdepth(self, root):
        if not root:
            return 0

        left = self.maxdepth(root.left)
        right = self.maxdepth(root.right)

        self.diameter = max(self.diameter, left + right)

        return max(left, right) + 1
