"""
给定一棵二叉树中的两个节点 p 和 q，返回它们的最近公共祖先节点（LCA）。

每个节点都包含其父节点的引用（指针）。Node的定义如下：

class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
根据维基百科中对最近公共祖先节点的定义：“两个节点 p 和 q 在二叉树 T 中的最近公共祖先节点是后代节点中既包括 p又包括q的最深节点（我们允许一个节点为自身的一个后代节点）”。一个节点 x的后代节点是节点x 到某一叶节点间的路径中的节点 y。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/lowest-common-ancestor-of-a-binary-tree-iii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def lowestCommonAncestor(self, p, q):
        """
        :type node: Node
        :rtype: Node
        """
        if not p or not q:
            return

        point1 = p
        point2 = q

        while point1 != point2:
            if point1:
                point1 = point1.parent
            else:
                point1 = q

            if point2:
                point2 = point2.parent
            else:
                point2 = p

        return point1
