"""
给你一个整数数组 nums ，你可以对它进行一些操作。

每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i] + 1 的元素。

开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-and-earn
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

分析：
选择任意一个nums[i]，删除它并获得nums[i]的点数，之后删除所有值等于nums[i]-1,nums[i]+1的元素，这代表，所有和nums[i]值相同的数字都被删除了。
统计相同元素的数字个数为sum(i), 删除x时，则可以获得sum(i)个点数，但是无法选择i-1元素或i+1元素，即不能相邻，也等于打家劫舍问题。
"""


class Solution:
    def deleteAndEarn(self, nums) -> int:
        all = [0] * (max(nums) + 1)
        for n in nums:
            all[n] += n

        return self.rob(all)

    def rob(self, nums) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)

        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])

        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.deleteAndEarn([3, 4, 2]))
