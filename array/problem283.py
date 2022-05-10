"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

请注意 ，必须在不复制数组的情况下原地对数组进行操作。
"""


class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

            fast += 1

        nums[slow:] = [0] * len(nums[slow:])
        print(nums)

    def moveZeroes2(self, nums: list) -> None:
        """
        如果不要求非零元素的相对顺序，则可以考虑此方法
        :param nums:
        :return:
        """
        left = 0
        right = len(nums)

        while left < right:
            if nums[left] == 0:
                right -= 1
                nums[left], nums[right] = nums[right], nums[left]
            else:
                left += 1

        print(nums)


if __name__ == '__main__':
    s = Solution()
    s.moveZeroes([0, 1, 0, 2, 3, 0, 4, 2])
    s.moveZeroes2([0, 1, 0, 2, 3, 0, 4, 2])
    s.moveZeroes2([])
