"""
给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。
"""

from binarytree.treenode import TreeNode, create_tree


class Solution:
    def levelOrder(self, root: TreeNode):
        if not root:
            return []

        q = [root]

        res = []
        while q:
            cur_level = []
            next_nodes = []
            for cur in q:
                cur_level.append(cur.val)
                if cur.left:
                    next_nodes.append(cur.left)
                if cur.right:
                    next_nodes.append(cur.right)

            q = next_nodes
            res.append(cur_level)

        return res


if __name__ == '__main__':
    s = Solution()
    t = create_tree([0, 1, 2, 3, 4, 5, 6])
    res = s.levelOrder(t)
    for r in res:
        print(r)
