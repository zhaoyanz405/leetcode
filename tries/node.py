class TrieNode:
    cap = 256

    def __init__(self, val=None):
        self.val = val
        self.children = [None] * self.cap

    @staticmethod
    def get_node(node, k):
        """
        search k from node
        :param node:
        :param k:
        :return:
        """
        p = node
        for c in k:
            if p is None:
                return

            p = p.children[ord(c)]

        return p

    @classmethod
    def put(cls, node, k, v, pos):
        if not node:
            node = cls()

        if pos == len(k):
            node.val = v
            return node

        c = ord(k[pos])
        node.children[c] = cls.put(node.children[c], k, v, pos + 1)
        return node

    def remove(self, k):
        self._remove_node(self, k, 0)

    @classmethod
    def _remove_node(cls, node, k, pos):
        if node is None:
            return

        if pos == len(k):
            node.val = None
        else:
            c = k[pos]
            node.children[c] = cls._remove_node(node.children[c], k, pos + 1)

        if node.val is not None:
            return node

        for child in node.children:
            if child is not None:
                return child

        return


if __name__ == '__main__':
    pass
