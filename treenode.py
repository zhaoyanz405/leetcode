import math
from queue import Queue


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    @property
    def depth(self):
        return self._get_depth(self)

    def _get_depth(self, node):
        if not node:
            return 0

        left = self._get_depth(node.left)
        right = self._get_depth(node.right)
        return max(left, right) + 1

    def level_traverse(self):
        res = []

        queue = Queue()
        queue.put(self)

        while not queue.empty():
            node = queue.get()
            res.append(node.val)

            if node.left:
                queue.put(node.left)

            if node.right:
                queue.put(node.right)

        return res

    def in_order_traverse(self):
        return self._in_order_traverse(self)

    def _in_order_traverse(self, node):
        res = []
        if node is None:
            return res

        if node.left:
            res += self._in_order_traverse(node.left)

        res.append(node.val)

        if node.right:
            res += self._in_order_traverse(node.right)

        return res

    def print(self):
        in_orders = self.in_order_traverse()
        level_orders = self.level_traverse()

        map_level = {}
        # 由于叶节点的位置确定后其他节点的位置才可以确定，因此先尝试压栈，直接通过层次遍历的逆序进行处理
        last_start = int(math.pow(2, self.depth - 1)) - 1
        last_levels = level_orders[last_start:]

        # 偶数层是节点，奇数层是树枝
        print(last_levels)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "TreeNode{%s}, left{%s}, right{%s}" % (self.val, str(self.left), str(self.right))


def create_tree(l: list, idx: int = 0):
    """
    从idx位置开始创建树
    :param l: 输入的数组
    :param idx: 开始位置
    :return: TreeNode
    """
    if idx >= len(l):
        return

    node = TreeNode(l[idx])
    node.left = create_tree(l, 2 * idx + 1)
    node.right = create_tree(l, 2 * idx + 2)
    return node


if __name__ == '__main__':
    n = create_tree(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
    n.print()
