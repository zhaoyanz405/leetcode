from graph.uf import UnionFind


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

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for row in range(m):
            for col in range(n):
                if board[row][col] == sign:
                    for d in dirs:
                        r = row + d[0]
                        c = col + d[1]
                        if r < m and c < n and board[r][c] == sign:
                            uf.union(r * n + c, row * n + col)

        for row in range(m):
            for col in range(n):
                if not uf.connected(row * n + col, dummy):
                    board[row][col] = "X"


if __name__ == '__main__':
    data = [["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]]
    s = Solution()
    s.solve(data)
    print(data)
