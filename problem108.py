"""
给你一个整数数组 nums ，其中元素已经按 升序 排列，请你将其转换为一棵 高度平衡 二叉搜索树。

高度平衡 二叉树是一棵满足「每个节点的左右两个子树的高度差的绝对值不超过 1 」的二叉树。



来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from treenode import TreeNode


class Solution:
    def sortedArrayToBST(self, nums):
        n = len(nums)
        if n == 0: return None
        return TreeNode(
            nums[n // 2],
            self.sortedArrayToBST(nums[0: (n // 2)]),
            self.sortedArrayToBST(nums[(n // 2) + 1:])
        )
