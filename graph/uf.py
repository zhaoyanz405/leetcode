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


class Solution:
    def solve(self, board: list) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        uf = UnionFind(m * n + 1)
        dummy = m * n

        sign = "O"

        for i in range(m):
            if board[i][0] == sign:
                uf.union(i * n + 0, dummy)

            if board[i][n - 1] == sign:
                uf.union(i * n + n - 1, dummy)

        for i in range(n):
            if board[0][i] == sign:
                uf.union(i, dummy)
            if board[m - 1][i] == sign:
                uf.union((m - 1) * n + i, dummy)

        for row in range(m):
            for col in range(n):
                if not uf.connected(row * n + col, dummy):
                    board[row][col] = "X"


if __name__ == '__main__':
    data = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    s = Solution()
    s.solve(data)
    print(data)
