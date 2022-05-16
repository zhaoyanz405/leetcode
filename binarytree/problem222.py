"""
给你一棵 完全二叉树 的根节点 root ，求出该树的节点个数。

完全二叉树 的定义如下：在完全二叉树中，除了最底层节点可能没填满外，其余每层节点数都达到最大值，并且最下面一层的节点都集中在该层最左边的若干位置。若最底层为第 h 层，则该层包含 1~ 2h 个节点。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/count-complete-tree-nodes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
import math


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        l = root
        r = root

        hl = hr = 0

        # 沿左侧计算高度
        while l:
            l = l.left
            hl += 1

        # 沿右侧计算高度
        while r:
            r = r.right
            hr += 1

        if hl == hr:
            # 满二叉树
            return int(math.pow(2, hl)) - 1

        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
