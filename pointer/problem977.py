class Solution:
    def sortedSquares(self, nums: list) -> list:
        p1 = self.find_first_positive_number(nums)
        res = []

        p2 = p1 + 1
        while p1 >= 0 and p2 <= len(nums) - 1:
            n1 = nums[p1] * nums[p1]
            n2 = nums[p2] * nums[p2]
            if n1 <= n2:
                res.append(n1)
                p1 -= 1
            else:
                res.append(n2)
                p2 += 1

        while p1 >= 0:
            n1 = nums[p1] * nums[p1]
            res.append(n1)
            p1 -= 1

        while p2 < len(nums):
            n2 = nums[p2] * nums[p2]
            res.append(n2)
            p2 += 1

        return res

    def find_first_positive_number(self, nums):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + int((right - left) >> 1)
            if nums[mid] >= 0:
                right = mid - 1
            else:
                left = mid + 1

        return left


if __name__ == '__main__':
    s = Solution()
    print(s.find_first_positive_number([-4]))
