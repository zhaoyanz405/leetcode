"""
给定一棵二叉树 root，返回所有重复的子树。

对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。

如果两棵树具有相同的结构和相同的结点值，则它们是重复的。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-duplicate-subtrees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def __init__(self):
        self.countmap = {}
        self.nodemap = {}

    def findDuplicateSubtrees(self, root) -> list:
        self.traverse(root)
        return list(self.nodemap.values())

    def traverse(self, root):
        if not root:
            return '#'

        left = self.traverse(root.left)
        right = self.traverse(root.right)

        subtree = str(left) + ',' + str(right) + ',' + str(root.val)

        if subtree not in self.countmap:
            self.countmap[subtree] = 0

        self.countmap[subtree] += 1
        if self.countmap[subtree] > 1:
            self.nodemap[subtree] = root

        return subtree
