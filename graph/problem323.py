from graph.uf import UnionFind


class Solution:
    def countComponents(self, n: int, edges: list) -> int:
        uf = UnionFind(n)
        for n1, n2 in edges:
            uf.union(n1, n2)

        return uf.count


if __name__ == '__main__':
    print(Solution().countComponents(4, [[2, 3], [1, 2], [1, 3]]))
