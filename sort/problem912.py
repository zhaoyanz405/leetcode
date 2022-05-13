"""
给你一个整数数组 nums，请你将该数组升序排列。
"""


class Solution:
    def sortArray(self, nums: list) -> list:
        if len(nums) < 2:
            return nums

        mid = int(len(nums) >> 1)
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        temp = []
        p1 = 0
        p2 = 0

        while p1 < len(left) and p2 < len(right):
            if left[p1] <= right[p2]:
                temp.append(left[p1])
                p1 += 1
            else:
                temp.append(right[p2])
                p2 += 1

        if p1 < len(left):
            temp += left[p1:]

        if p2 < len(right):
            temp += right[p2:]

        return temp


if __name__ == '__main__':
    s = Solution()
    print(s.sortArray([7, 2, 3, 5, 1, 2, 7, 3, 4]))
