class Solution:
    def __init__(self):
        self.max_res = float('-inf')

    def maxPathSum(self, root) -> int:
        self.max_(root)
        return self.max_res

    def max_(self, node):
        if not node:
            return 0

        leftmax = max(self.max_(node.left), 0)
        rightmax = max(self.max_(node.right), 0)

        self.max_res = max(self.max_res, leftmax + rightmax + node.val)
        return node.val + max(leftmax, rightmax)


if __name__ == '__main__':
    from binarytree.treenode import create_tree

    print(Solution().maxPathSum(create_tree([-3])))
