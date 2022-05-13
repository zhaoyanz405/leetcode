"""
给你一个整数数组 nums ，按要求返回一个新数组counts 。
数组 counts 有该性质： counts[i] 的值是 nums[i] 右侧小于nums[i] 的元素的数量。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/count-of-smaller-numbers-after-self
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Count:
    def __init__(self, idx=None, val=None, count=0):
        self.idx = idx
        self.val = val
        self.count = count


class Solution:
    def countSmaller(self, nums: list) -> list:
        clist = []
        for i, n in enumerate(nums):
            clist.append(Count(i, n))

        self.sort(clist)

        res = [0] * len(nums)
        for c in clist:
            res[c.idx] = c.count

        return res

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
            if n1[p1].val <= n2[p2].val:
                n1[p1].count += p2  # 只能与n2中前p2个元素组成逆序对
                temp.append(n1[p1])
                p1 += 1
            elif n1[p1].val > n2[p2].val:
                temp.append(n2[p2])
                p2 += 1

        while p1 < len(n1):
            n1[p1].count += p2  # 只能与n2中前p2个元素组成逆序对
            temp.append(n1[p1])
            p1 += 1

        while p2 < len(n2):
            temp.append(n2[p2])
            p2 += 1

        return temp
