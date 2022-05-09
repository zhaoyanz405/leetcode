"""
给定一个二维矩阵 matrix，以下类型的多个请求：

计算其子矩形范围内元素的总和，该子矩阵的 左上角 为 (row1,col1) ，右下角 为 (row2,col2) 。
实现 NumMatrix 类：

NumMatrix(int[][] matrix)给定整数矩阵 matrix 进行初始化
int sumRegion(int row1, int col1, int row2, int col2)返回 左上角 (row1,col1)、右下角(row2,col2) 所描述的子矩阵的元素 总和 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/range-sum-query-2d-immutable
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class NumMatrix:

    def __init__(self, matrix):
        m = len(matrix) + 1
        n = len(matrix[0]) + 1
        # self.pre = [[0] * n] * m  # bugs?
        # it equals
        # row = [0] * n
        # self.pre = [row] * m
        self.pre = [[0] * n for _ in range(m)]

        for i in range(1, m):
            for j in range(1, n):
                self.pre[i][j] = self.pre[i - 1][j] + self.pre[i][j - 1] - self.pre[i - 1][j - 1] + matrix[i - 1][j - 1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.pre[row2 + 1][col2 + 1] - self.pre[row1][col2 + 1] - self.pre[row2 + 1][col1] + self.pre[row1][col1]


if __name__ == '__main__':
    s = NumMatrix([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(s.sumRegion(1, 1, 2, 2))
