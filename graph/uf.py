class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parent = [-1] * n
        for i in range(n):
            self.parent[i] = i

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)

        # 使p，q具有相同的根节点，即为连接
        if root_p == root_q:
            return

        self.parent[root_q] = root_p
        self.count -= 1

    def find(self, x):
        # 找到根节点
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def connected(self, p, q):
        return self.find(p) == self.find(q)
