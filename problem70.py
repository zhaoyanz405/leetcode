"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1:
            return 1
        # 1. dp记录了第i阶台阶的走法
        dp = [0] * (n + 1)
        # 2. 要跳到第i阶台阶，要么从i-1阶起跳，要么从i-2阶起跳
        # 因此，dp[i] = dp[i-1] + dp[i-2]
        # 3. dp数组初始化，
        # 在第1阶台阶时，dp只有一种跳法
        dp[1] = 1
        # 在第2阶台阶时，dp有两种跳法
        dp[2] = 2
        # 4. 后序阶以来前序阶，因此需要顺序遍历
        # 5. 举例推导
        # dp[0] = 0, dp[1] = 1, dp[2] = 2, dp[3] = 3
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.climbStairs(3))