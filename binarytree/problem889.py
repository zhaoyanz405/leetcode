"""
给定两个整数数组，preorder和 postorder ，其中 preorder 是一个具有 无重复 值的二叉树的前序遍历，postorder 是同一棵树的后序遍历，重构并返回二叉树。

如果存在多个答案，您可以返回其中 任何 一个。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/construct-binary-tree-from-preorder-and-postorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from binarytree.treenode import TreeNode


class Solution:
    def constructFromPrePost(self, preorder: list, postorder: list) -> TreeNode:
        if not preorder or not postorder:
            return

        if len(preorder) == 1:
            return TreeNode(preorder[0])

        root = preorder[0]
        left = preorder[1]

        post_map = {n: i for i, n in enumerate(postorder)}
        left_idx = post_map[left]
        leftpart_size = left_idx + 1

        left_preorder = preorder[1:leftpart_size + 1]
        right_preorder = preorder[leftpart_size + 1:]

        left_postorder = postorder[:left_idx + 1]
        right_postorder = postorder[left_idx + 1:-1]

        node = TreeNode(root)
        node.left = self.constructFromPrePost(left_preorder, left_postorder)
        node.right = self.constructFromPrePost(right_preorder, right_postorder)
        return node


if __name__ == '__main__':
    s = Solution()
    s.constructFromPrePost(preorder=[1, 2, 4, 5, 3, 6, 7], postorder=[4, 5, 2, 6, 7, 3, 1])
