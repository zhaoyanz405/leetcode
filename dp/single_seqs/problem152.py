"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

子数组 是数组的连续子序列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def maxProduct(self, nums) -> int:
        if len(nums) < 2:
            return nums[0]

        dpmax = [0] * len(nums)
        dpmin = [0] * len(nums)
        dpmax[0] = nums[0]
        dpmin[0] = nums[0]

        for i in range(1, len(nums)):
            dpmax[i] = max(nums[i], dpmax[i - 1] * nums[i], dpmin[i - 1] * nums[i])
            dpmin[i] = min(nums[i], dpmax[i - 1] * nums[i], dpmin[i - 1] * nums[i])

        return max(dpmax)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-2, 3, -4]))
    print(s.maxProduct([2, 3, -2, 4]))
    print(s.maxProduct([-2]))
    print(s.maxProduct([-2, 1]))
    print(s.maxProduct([-2, 1, -1]))
    print(s.maxProduct([-3,-1,-1]))
    print(s.maxProduct([-4,-3]))
    print(s.maxProduct([2,-5,-2,-4,3]))
