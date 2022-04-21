"""
给定一个非负整数数组 nums ，你最初位于数组的 第一个下标 。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个下标。

示例1：

输入：nums = [2,3,1,1,4]
输出：true
解释：可以先跳 1 步，从下标 0 到达下标 1, 然后再从下标 1 跳 3 步到达最后一个下标。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/jump-game
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def canJump(self, nums) -> bool:
        return self.canJump2(nums)

    def canJump1(self, nums) -> bool:
        # 1. 确定dp[i]的含义, 第i个位置能否达到
        # 2. 确定dp推导式
        # 分析，如果第i个位置可以达到，则(i, nums[i] + 1)都可以达到。
        if len(nums) < 2:
            return True

        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            if dp[i]:
                for j in range(i + 1, min(nums[i] + i + 1, len(nums))):
                    dp[j] = True

        return dp[-1]

    def canJump2(self, nums) -> bool:
        k = 0
        for i in range(len(nums)):
            if i > k:
                return False

            k = max(k, i + nums[i])

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))
    print(s.canJump([3, 2, 1, 0, 4]))
