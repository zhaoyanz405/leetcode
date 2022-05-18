"""
给你一个整数数组 coins ，表示不同面额的硬币；以及一个整数 amount ，表示总金额。

计算并返回可以凑成总金额所需的 最少的硬币个数 。如果没有任何一种硬币组合能组成总金额，返回 -1 。

你可以认为每种硬币的数量是无限的。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/coin-change
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution(object):
    def coinChange(self, coins, amount):
        if amount < 0:
            return -1

        # 确定dp数组的含义， dp表示金额为i时，最少需要dp[i]个硬币
        # 确定状态dp[i] = min(dp[i], dp[i - coin] + 1)
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        for i in range(amount + 1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i], dp[i - c] + 1)

        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    print(s.coinChange([2147483647], 2))