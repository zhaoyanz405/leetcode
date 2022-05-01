"""
给定一个未排序的整数数组 nums ， 返回最长递增子序列的个数 。

注意 这个数列必须是 严格 递增的。

 

示例 1:

输入: [1,3,5,4,7]
输出: 2
解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
示例 2:

输入: [2,2,2,2,2]
输出: 5
解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findNumberOfLIS(self, nums) -> int:
        count = [1] * len(nums)
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[j] + 1 > dp[i]:
                        dp[i] = dp[j] + 1
                        count[i] = count[j]
                    elif dp[j] + 1 == dp[i]:
                        count[i] += count[j]

        maxn = max(dp)
        return sum(count[i] for i, v in enumerate(dp) if v == maxn)


if __name__ == '__main__':
    s = Solution()
    print(s.findNumberOfLIS([1, 3, 5, 4, 7]))
    print(s.findNumberOfLIS([2, 2, 2, 2, 2]))
    print(s.findNumberOfLIS([1, 2, 4, 3, 5, 4, 7, 2]))
