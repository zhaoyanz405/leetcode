"""
在n x n的网格grid中，我们放置了一些与 x，y，z 三轴对齐的1 x 1 x 1立方体。

每个值v = grid[i][j]表示 v个正方体叠放在单元格(i, j)上。

现在，我们查看这些立方体在 xy、yz和 zx平面上的投影。

投影就像影子，将 三维 形体映射到一个 二维 平面上。从顶部、前面和侧面看立方体时，我们会看到“影子”。

返回 所有三个投影的总面积 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/projection-area-of-3d-shapes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def projectionArea(self, grid) -> int:
        total = 0
        col_map = {}
        for row in grid:
            for idx, v in enumerate(row):  # 选出每一列中的最大值
                if v:
                    total += 1

                if idx not in col_map:
                    col_map[idx] = 0

                col_map[idx] = max(col_map[idx], v)

            total += max(row)

        total += sum(col_map.values())
        return total

    def projectionArea2(self, grid) -> int:
        top = sum(v > 0 for row in grid for v in row)
        # a = [1, 2, 3, -1, 4]
        # print(v > 0 for v in a)
        # < generator
        # object < genexpr > at
        # 0x10a5e0740 >
        # print(list(v > 0 for v in a))
        # [True, True, True, False, True]
        # print(sum(list(v > 0 for v in a)))
        # 4
        left = sum(max(row) for row in grid)
        front = sum(max(col) for col in zip(*grid))
        return top + left + front


if __name__ == '__main__':
    s = Solution()
    print(s.projectionArea([[1, 0], [0, 2]]))
    print(s.projectionArea2([[1, 0], [0, 2]]))
