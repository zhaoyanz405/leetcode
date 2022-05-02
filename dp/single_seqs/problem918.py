"""
给定一个长度为 n 的环形整数数组nums，返回nums的非空 子数组 的最大可能和。

环形数组意味着数组的末端将会与开头相连呈环状。形式上， nums[i] 的下一个元素是 nums[(i + 1) % n] ， nums[i]的前一个元素是 nums[(i - 1 + n) % n] 。

子数组 最多只能包含固定缓冲区nums中的每个元素一次。形式上，对于子数组nums[i], nums[i + 1], ..., nums[j]，不存在i <= k1, k2 <= j其中k1 % n == k2 % n。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-sum-circular-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxSubarraySumCircular(self, nums) -> int:
        curmax = 0
        curmin = 0

        maxsum = nums[0]
        minsum = nums[0]

        for n in nums:
            curmax = max(n, curmax + n)
            maxsum = max(maxsum, curmax)

            curmin = min(n, curmin + n)
            minsum = min(minsum, curmin)

        if maxsum > 0:
            return max(maxsum, sum(nums) - minsum)
        else:
            return maxsum


if __name__ == '__main__':
    s = Solution()
    print(s.maxSubarraySumCircular([1, -2, 3, -2]))
    print(s.maxSubarraySumCircular([5, -3, 5]))
