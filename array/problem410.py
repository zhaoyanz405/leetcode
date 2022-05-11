"""
给定一个非负整数数组 nums 和一个整数 m ，你需要将这个数组分成 m 个非空的连续子数组。

设计一个算法使得这 m 个子数组各自和的最大值最小。
"""


class Solution:
    def splitArray(self, nums: list, m: int) -> int:
        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + int((right - left) >> 1)
            cost = self.load(nums, mid)
            if cost <= m:
                right = mid
            elif cost > m:
                left = mid + 1

        return left

    def load(self, weights, x):
        days = 1
        cur = 0

        for w in weights:
            cur += w
            if cur > x:
                cur = w
                days += 1

        return days
