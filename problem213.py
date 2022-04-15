"""
你是一个专业的小偷，计划偷窃沿街的房屋，每间房内都藏有一定的现金。这个地方所有的房屋都 围成一圈 ，这意味着第一个房屋和最后一个房屋是紧挨着的。同时，相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警 。

给定一个代表每个房屋存放金额的非负整数数组，计算你 在不触动警报装置的情况下 ，今晚能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def rob(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums)

        rob_from_dp0 = self._rob(nums[:-1], nums[0], nums[0])
        rob_from_dp1 = self._rob(nums, 0, nums[1])

        return max(rob_from_dp0, rob_from_dp1)

    def _rob(self, nums, init_dp0, init_dp1) -> int:
        dp = [0] * len(nums)

        dp[0] = init_dp0
        dp[1] = init_dp1

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.rob(nums=[0, 0]))
