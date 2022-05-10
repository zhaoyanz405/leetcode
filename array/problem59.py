"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。
"""


class Solution:
    def generateMatrix(self, n: int):
        top = 0
        left = 0
        right = n - 1
        bottom = n - 1

        matrix = [[0] * n for _ in range(n)]
        c = 1
        while c <= n * n:
            # 向右
            if top <= bottom:
                for j in range(left, right + 1):
                    matrix[top][j] = c
                    c += 1

                top += 1

            # 向下
            if left <= right:
                for j in range(top, bottom + 1):
                    matrix[j][right] = c
                    c += 1

                right -= 1

            # 向左
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    matrix[bottom][j] = c
                    c += 1

                bottom -= 1

            # 向上
            if left <= right:
                for j in range(bottom, top - 1, -1):
                    matrix[j][left] = c
                    c += 1

                left += 1

        return matrix


if __name__ == '__main__':
    s = Solution()
    m = s.generateMatrix(3)
    for row in m:
        print(row)
