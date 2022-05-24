"""
给你一个由'1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/number-of-islands
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def numIslands(self, grid: list) -> int:
        res = 0
        # visited = [[False] * len(grid[0]) for _ in range(len(grid))]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    res += 1
                    # 淹没这块陆地
                    self.flood(grid, i, j)

        return res

    def flood(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
            return
        #
        # if visited[i][j]:
        #     return
        #
        # visited[i][j] = True
        if grid[i][j] == '0':
            return

        grid[i][j] = '0'
        self.flood(grid, i - 1, j)
        self.flood(grid, i, j + 1)
        self.flood(grid, i + 1, j)
        self.flood(grid, i, j - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.numIslands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))
