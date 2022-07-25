
class TrieMap:

    def __init__(self):
        self._size = 0
        self._R = 256
        self._root: TrieNode = None

    def put(self, k, v):
        if k not in self:
            self._size += 1

        self._root.put(k, v)

    def remove(self, k):
        if k not in self:
            return

        self._root.remove(k)
        self._size -= 1

    def get(self, k):
        if not self._root:
            return
        target = self._root.get_node(k)
        if not target or not target.val:
            return

        return target.val

    def __contains__(self, k):
        return self.get(k) is not None

    def shortest_prefix_of(self, query):
        if not query:
            return ""

        p = self._root
        for i, c in enumerate(query):
            if p is None:
                return ""

            if p.val is not None:
                # find a prefix
                return query[:i]

            p = p.children[c]

        if p is not None and p.val is not None:
            return query

        return ""

    def longest_prefix_of(self, query):
        p = self._root
        max_len = 0

        for i, c in enumerate(query):
            if p is None:
                break

            if p.val is not None:
                # find a prefix
                max_len = i

            p = p.children[c]

        if p is not None and p.val is not None:
            return query

        return query[:max_len]

    def keys_with_prefix(self, prefix):
        res = []
        target = self._root.get_node(prefix)
        if target is None:
            return res

    def has_key_with_prefix(self, prefix):
        return self._root.get_node(prefix) is not None

    def keys_with_pattern(self, pattern):
        pass

    def has_key_with_pattern(self, pattern):
        pass

    def size(self):
        return self._size

    def _traverse(self, node: TrieNode, path: str) -> list:
        res = []
        if node is None:
            return res

        if node.val is None:
            res.append(path)

        for c in range(self._R):
            path += c
            res += self._traverse(node.children[c], path)
            path = path[:-1]

        return res


if __name__ == '__main__':
    map = TrieMap()
    map.put('test', 6)