"""
给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。

叶子节点 是指没有子节点的节点。
"""
import copy

from binarytree.treenode import create_tree


class Solution:
    def binaryTreePaths(self, root):
        res = set()
        if not root:
            return res

        self.post_order_traverse(root, [], res)
        return res

    def post_order_traverse(self, root, path, res):
        if not root:
            res.add("->".join(map(str, path)))
            return

        path.append(root.val)
        self.post_order_traverse(root.left, path, res)
        self.post_order_traverse(root.right, path, res)
        path.pop()


if __name__ == '__main__':
    root = create_tree([1, 2, 3, 4, 5, 6])
    print(root.level_traverse())
    print(Solution().binaryTreePaths(root))
