"""
序列化是将一个数据结构或者对象转换为连续的比特位的操作，进而可以将转换后的数据存储在一个文件或者内存中，同时也可以通过网络传输到另一个计算机环境，采取相反方式重构得到原数据。

请设计一个算法来实现二叉树的序列化与反序列化。这里不限定你的序列 / 反序列化算法执行逻辑，你只需要保证一个二叉树可以被序列化为一个字符串并且将这个字符串反序列化为原始的树结构。

提示: 输入输出格式与 LeetCode 目前使用的方式一致，详情请参阅LeetCode 序列化二叉树的格式。你并非必须采取这种方式，你也可以采用其他的方法解决这个问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/serialize-and-deserialize-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Codec:
    sep = ','
    null = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        res = []
        self.preorder_traverse(root, res)
        return self.sep.join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        nodes = data.split(self.sep)
        return self._deserialize(nodes)

    def _deserialize(self, nodes):
        if not nodes:
            return

        rootval = nodes[0]
        del nodes[0]
        if rootval == self.null:
            return TreeNode(None)

        n = TreeNode(int(rootval))
        n.left = self._deserialize(nodes)
        n.right = self._deserialize(nodes)
        return n

    def preorder_traverse(self, root, res):

        if not root:
            return

        val = root.val
        if not val:
            val = self.null

        res.append(str(val))

        self.preorder_traverse(root.left, res)
        self.preorder_traverse(root.right, res)


if __name__ == '__main__':
    from binarytree.treenode import create_tree, TreeNode

    t = create_tree([1, 2, 3, None, None, 4, 5])
    print(t.level_traverse())

    c = Codec()
    res = c.serialize(t)
    print(res)
    n = c.deserialize(res)
    print(n.level_traverse())
