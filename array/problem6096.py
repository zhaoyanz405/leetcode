class Solution:
    def successfulPairs(self, spells: list, potions: list, success: int) -> list:
        potions.sort()
        lp = len(potions)
        res = [0] * len(spells)
        for i, s in enumerate(spells):
            j = self.find(potions, success / s)
            if s * potions[j] >= success:
                res[i] = lp - j
            else:
                res[i] = lp - j - 1

        return res

    def find(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + int((right - left) >> 1)
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] >= target:
                right = mid - 1

        return left


if __name__ == '__main__':
    s = Solution()
    print(s.successfulPairs([3, 1, 2],
                            [8, 5, 8],
                            16
                            ))
