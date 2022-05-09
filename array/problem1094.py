"""
车上最初有capacity个空座位。车只能向一个方向行驶（也就是说，不允许掉头或改变方向）

给定整数capacity和一个数组 trips , trip[i] = [numPassengersi, fromi, toi]表示第 i 次旅行有numPassengersi乘客，接他们和放他们的位置分别是fromi和toi。这些位置是从汽车的初始位置向东的公里数。

当且仅当你可以在所有给定的行程中接送所有乘客时，返回true，否则请返回 false。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/car-pooling
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def carPooling(self, trips: list, capacity: int) -> bool:
        diff = [0] * 1000
        for num, fr, to in trips:
            diff[fr] += num
            if to < len(diff):
                diff[to] -= num

        res = [0] * len(diff)
        res[0] = diff[0]
        for i in range(len(diff)):
            res[i] = res[i - 1] + diff[i]
            if res[i] > capacity:
                return False

        return True


if __name__ == '__main__':
    s = Solution()
    res = s.carPooling([[2, 1, 5], [3, 5, 7]], 3)
    print(res)
