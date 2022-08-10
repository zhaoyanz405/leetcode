"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。
"""


class Solution:
    def findKthLargest(self, nums: list, k: int) -> int:
        pass

    def partition(self, nums, L, R):
        less = L - 1
        more = R

        while L < R:
            if nums[L] < nums[R]:
                less += 1
                more -= 1
                nums[less], nums[more] = nums[more], nums[less]



if __name__ == '__main__':
    s = Solution()
    nums = [3, 1, 2, 4, 5]
    res = s.sort(nums, 0, len(nums))
    print(nums, res)
