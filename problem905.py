"""
给你一个整数数组 nums，将 nums 中的的所有偶数元素移动到数组的前面，后跟所有奇数元素。

返回满足此条件的 任一数组 作为答案。
"""


class Solution:
    def sortArrayByParity(self, nums):
        right = len(nums)
        left = 0
        while left < right:
            if nums[left] % 2 == 0:
                left += 1
            else:
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]

        return nums
