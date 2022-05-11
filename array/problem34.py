"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

进阶：

你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def searchRange(self, nums: list, target: int) -> list:
        if not nums:
            return [-1, -1]

        return [
            self.search_left(nums, target),
            self.search_right(nums, target)
        ]

    def search_left(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) >> 1)
            if nums[mid] >= target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        if left >= len(nums) or nums[left] != target:
            return -1

        return left

    def search_right(self, nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) >> 1)
            if nums[mid] <= target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if right < 0 or nums[right] != target:
            return -1

        return right


if __name__ == '__main__':
    s = Solution()
    print(s.search_left([2, 2], 3))
    print(s.search_right([2, 2], 3))
