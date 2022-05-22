class Solution:
    def threeSum(self, nums: list) -> list:
        nums.sort()
        res = list()

        i = 0
        while i < len(nums):
            cur = nums[i]
            twos = self.twosum(nums[i + 1:], 0 - nums[i])
            for t in twos:
                print(t)
                res.append([nums[i], *t])

            while i < len(nums) and cur == nums[i]:
                i += 1

        return res

    def twosum(self, nums, target):
        left = 0
        right = len(nums) - 1

        res = []
        while left < right:
            s = nums[left] + nums[right]
            if s < target:
                left += 1
            elif s == target:
                res.append([nums[left], nums[right]])
                cur_left = nums[left]
                while left < right and cur_left == nums[left]:
                    left += 1

                cur_right = nums[right]
                while left < right and cur_right == nums[right]:
                    right -= 1

            elif s > target:
                right -= 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-4, -1, -1, 1, 0, 2]))
    # print(s.twosum([1, 2, 3, 2, 1, 2, 1], 3))
