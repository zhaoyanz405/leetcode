class Solution:
    def increasingTriplet(self, nums: list) -> bool:
        # 定义dp[i]为以i位置结尾的，最长递增子序列的长度。
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            if nums[i] >= nums[i - 1]:
                dp[i] = dp[i - 1] + 1
            elif i - 2 >= 0 and nums[i] >= nums[i - 2]:
                dp[i] = dp[i - 2] + 1
            if dp[i] >= 3:
                return True

        return False

    def increasingTriplet2(self, nums: list) -> bool:
        n = len(nums)
        if n < 3:
            return False

        left_min = [0] * len(nums)
        left_min[0] = nums[0]

        right_max = [0] * len(nums)
        right_max[-1] = nums[-1]

        for i in range(1, len(nums)):
            left_min[i] = min(left_min[i - 1], nums[i])

        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        for i in range(1, n - 1):
            if left_min[i - 1] < nums[i] < right_max[i + 1]:
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    print(s.increasingTriplet2([20, 100, 10, 12, 5, 13]))
