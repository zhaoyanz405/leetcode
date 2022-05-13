"""
在数组中的两个数字，如果前面一个数字大于后面的数字，则这两个数字组成一个逆序对。输入一个数组，求出这个数组中的逆序对的总数。
"""


class Solution:
    def __init__(self):
        self.count = 0

    def reversePairs(self, nums: list) -> int:
        self.sort(nums)
        return self.count

    def sort(self, nums):
        if len(nums) < 2:
            return nums

        mid = int(len(nums) >> 1)
        left = self.sort(nums[:mid])
        right = self.sort(nums[mid:])

        return self.merge(left, right)

    def merge(self, n1, n2):
        temp = []

        p1 = p2 = 0
        while p1 < len(n1) and p2 < len(n2):
            if n1[p1] <= n2[p2]:
                temp.append(n1[p1])
                p1 += 1
                self.count += p2  # 只能与n2中前p2个元素组成逆序对
            elif n1[p1] > n2[p2]:
                temp.append(n2[p2])
                p2 += 1

        while p1 < len(n1):
            temp.append(n1[p1])
            p1 += 1
            self.count += p2

        while p2 < len(n2):
            temp.append(n2[p2])
            p2 += 1

        return temp


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([1, 3, 2, 3, 1]))
