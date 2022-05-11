"""
给定一个n个元素有序的（升序）整型数组nums 和一个目标值target ，写一个函数搜索nums中的 target，如果目标值存在返回下标，否则返回 -1。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def search(self, nums: list, target: int) -> int:
        if not nums:
            return -1

        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = left + int((right - left) >> 1)
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid - 1
            elif target > nums[mid]:
                left = mid + 1

        return -1


if __name__ == '__main__':
    s = Solution()
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=9))
    print(s.search(nums=[-1, 0, 3, 5, 9, 12], target=2))
