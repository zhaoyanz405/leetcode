"""
给定一个数组nums，如果i < j且nums[i] > 2*nums[j]我们就将(i, j)称作一个重要翻转对。

你需要返回给定数组中的重要翻转对的数量。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def __init__(self):
        self.count = 0

    def reversePairs(self, nums: list) -> int:
        self.count = 0
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
        end = []
        while p1 < len(n1) and p2 < len(n2):
            if n1[p1] <= n2[p2]:
                # 在此处搜索是否有符合条件的组合
                # todo 优化
                for i in range(len(n2)):
                    if n2[i] in end:
                        self.count += 1
                        continue

                    if n1[p1] > n2[i] * 2:
                        self.count += 1
                        end.append(n2[i])

                temp.append(n1[p1])
                p1 += 1
            elif n1[p1] > n2[p2]:
                temp.append(n2[p2])
                p2 += 1

        while p1 < len(n1):
            # 在此处搜索是否有符合条件的组合
            for i in range(len(n2)):
                if n2[i] in end:
                    self.count += 1
                    continue

                if n1[p1] > n2[i] * 2:
                    self.count += 1
                    end.append(n2[i])

            temp.append(n1[p1])
            p1 += 1

        while p2 < len(n2):
            temp.append(n2[p2])
            p2 += 1

        return temp


if __name__ == '__main__':
    s = Solution()
    print(s.reversePairs([1, 3, 2, 3, 1]))
    print(s.reversePairs([2, 4, 3, 5, 1]))
