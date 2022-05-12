"""
给定一个不重复的整数数组nums 。最大二叉树可以用下面的算法从nums 递归地构建:

创建一个根节点，其值为nums 中的最大值。
递归地在最大值左边的子数组前缀上构建左子树。
递归地在最大值 右边 的子数组后缀上构建右子树。
返回nums 构建的 最大二叉树 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def constructMaximumBinaryTree(self, nums: list) -> TreeNode:
        if not nums:
            return

        value, idx = self.find_max(nums)

        node = TreeNode(value)
        node.left = self.constructMaximumBinaryTree(nums[:idx])

        node.right = None
        node.right = self.constructMaximumBinaryTree(nums[idx + 1:])

        return node

    def find_max(self, nums):
        value = float('-inf')
        index = 0
        for i, n in enumerate(nums):
            if n > value:
                value = n
                index = i

        return value, index


if __name__ == '__main__':
    s = Solution()
    s.constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
