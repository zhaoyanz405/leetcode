"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组 是数组中的一个连续部分。
"""


class Solution:
    def maxSubArray(self, nums) -> int:
        # 定义dp[i]为以nums[i]结尾的最大和
        # 状态转移公式dp[i] = nums[i]   if dp[i-1] <= 0
        #                   nums[i] + dp[i-1]  if dp[i-1] > 0
        if not nums:
            return 0

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = nums[i] + max(0, dp[i - 1])

        return max(dp)


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray([5, 4, -1, 7, 8]))
