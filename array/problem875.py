"""
珂珂喜欢吃香蕉。这里有 n 堆香蕉，第 i 堆中有piles[i]根香蕉。警卫已经离开了，将在 h 小时后回来。

珂珂可以决定她吃香蕉的速度 k （单位：根/小时）。每个小时，她将会选择一堆香蕉，从中吃掉 k 根。如果这堆香蕉少于 k 根，她将吃掉这堆的所有香蕉，然后这一小时内不会再吃更多的香蕉。

珂珂喜欢慢慢吃，但仍然想在警卫回来前吃掉所有的香蕉。

返回她可以在 h 小时内吃掉所有香蕉的最小速度 k（k 为整数）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/koko-eating-bananas
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minEatingSpeed(self, piles: list, h: int) -> int:
        left = 1
        right = 1000000000 + 1
        while left <= right:
            mid = left + int((right - left) >> 1)
            cost = self.eat(piles, mid)
            if cost <= h:
                right = mid - 1
            elif cost > h:
                left = mid + 1

        return left

    def eat(self, piles, k):
        """当以每小时k的速度吃时，吃完需要多长时间"""
        hours = 0
        for p in piles:
            hours += p // k
            if p % k:
                hours += 1

        return hours


if __name__ == '__main__':
    s = Solution()
    s.minEatingSpeed([2, 2], 2)
