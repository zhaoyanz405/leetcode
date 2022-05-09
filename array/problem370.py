"""
假设你有一个长度为n的数组，初始情况下所有的数字均为0，你将会被给出k​​​​​​​ 个更新的操作。

其中，每个操作会被表示为一个三元组：[startIndex, endIndex, inc]，你需要将子数组A[startIndex ... endIndex]（包括 startIndex 和 endIndex）增加inc。

请你返回k次操作后的数组。

示例:

输入: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
输出: [-2,0,3,5,3]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/range-addition
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:

    def __init__(self):
        self.nums = None
        self.diff = None

    def getModifiedArray(self, length: int, updates) -> list:
        self.nums = [0] * length
        self.diff = [0] * length

        for start, end, val in updates:
            self.incr(start, end, val)

        return self.recovery()

    def incr(self, start, end, val):
        self.diff[start] += val
        if end + 1 < len(self.diff):
            self.diff[end + 1] -= val

        print(self.recovery())

    def recovery(self):
        res = [0] * len(self.diff)
        res[0] = self.diff[0]
        for i in range(1, len(self.diff)):
            res[i] = res[i - 1] + self.diff[i]

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.getModifiedArray(5, [[1, 3, 2], [2, 4, 3], [0, 2, -2]]))
