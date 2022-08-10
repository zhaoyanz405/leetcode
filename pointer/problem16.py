"""
给你一个长度为 n 的整数数组nums和 一个目标值target。请你从 nums 中选出三个整数，使它们的和与target最接近。

返回这三个数的和。

假定每组输入只存在恰好一个解。
"""


class Solution:
    def threeSumClosest(self, nums: list, target: int) -> int:
        nums.sort()

        delta = float('inf')
        for i in range(len(nums)):
            diff = target - nums[i]
            s = nums[i] + self.twosumclosest(nums, abs(diff))
            if delta > abs(diff):
                delta = target - sum

    def twosumclosest(self, nums, target):
        left = 0
        right = len(nums) - 1

        delta = float('inf')

        while left < right:
            s = nums[right] + nums[left]
            delta = min(delta, abs(s - target))
            if s < target:
                left += 1
            elif s == target:
                return nums[left], nums[right]
            elif s > target:
                right -= 1

        return delta


if __name__ == '__main__':
    s = Solution()
    print(s.twosumclosest([1, 2, 3, 4, 5], 2.8))
