class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        sum_ = sum(nums)
        max_ = max(nums)
        return self.binary(nums, m, max_, sum_)

    def binary(self, nums, m, low, high):
        while low <= high:
            mid = low + int((high - low) >> 1)
            if self.is_valid(nums, m, mid):
                high = mid - 1
            else:
                low = mid + 1

        return low

    def is_valid(self, nums, m, sub_sum):
        cur = 0
        count = 0

        for n in nums:
            cur += n
            if cur > sub_sum:
                cur = n
                count += 1
                if count > m:
                    return False
        return True
