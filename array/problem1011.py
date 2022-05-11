"""
传送带上的包裹必须在 days 天内从一个港口运送到另一个港口。

传送带上的第 i个包裹的重量为weights[i]。每一天，我们都会按给出重量（weights）的顺序往传送带上装载包裹。我们装载的重量不会超过船的最大运载重量。

返回能在 days 天内将传送带上的所有包裹送达的船的最低运载能力。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/capacity-to-ship-packages-within-d-days
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def shipWithinDays(self, weights: list, days: int) -> int:
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + int((right - left) >> 1)
            cost = self.load(weights, mid)
            if cost <= days:
                right = mid
            elif cost > days:
                left = mid + 1

        return left

    def load(self, weights, x):
        """
        每天装在x重量，最终需要多少天可以完成
        :param weights:
        :param x:
        :return:
        """
        days = 1
        cur = 0

        for w in weights:
            cur += w
            if cur > x:
                cur = w
                days +=1

        return days


if __name__ == '__main__':
    s = Solution()
    print(s.shipWithinDays(weights=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], days=5))
