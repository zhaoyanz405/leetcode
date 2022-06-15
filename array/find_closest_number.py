class Solution:

    def find_closest_number(self, nums, target):
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = left + int((right - left) >> 1)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1

        if left > 1 and abs(nums[left - 1] - target) < abs(nums[left] - target):
            return left - 1

        return left


if __name__ == '__main__':
    s = Solution()
    print(s.find_closest_number([0, 1, 2, 3, 4, 5], 1.4))
