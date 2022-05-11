"""
给你一个 下标从 0 开始 的正整数数组w ，其中w[i] 代表第 i 个下标的权重。

请你实现一个函数pickIndex，它可以 随机地 从范围 [0, w.length - 1] 内（含 0 和 w.length - 1）选出并返回一个下标。选取下标 i的 概率 为 w[i] / sum(w) 。

例如，对于 w = [1, 3]，挑选下标 0 的概率为 1 / (1 + 3)= 0.25 （即，25%），而选取下标 1 的概率为 3 / (1 + 3)= 0.75（即，75%）。


来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/random-pick-with-weight
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from random import randint


class Solution:

    def __init__(self, w: list):
        self.presum = [0] * (len(w) + 1)
        for i in range(1, len(w) + 1):
            self.presum[i] = self.presum[i - 1] + w[i - 1]

    def pickIndex(self) -> int:
        target = randint(1, self.presum[-1])
        return self.search_left(self.presum, target) - 1

    def search_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) >> 1)
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return left


if __name__ == '__main__':
    s = Solution([1])

    res = []
    for i in range(10):
        res.append(s.pickIndex())

    print(res.count(0))
    print(res.count(1))
