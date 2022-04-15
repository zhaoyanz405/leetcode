"""
泰波那契序列Tn定义如下：

T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0的条件下 Tn+3 = Tn + Tn+1 + Tn+2

给你整数n，请返回第 n 个泰波那契数Tn 的值。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/n-th-tribonacci-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        if not n:
            return 0

        if n == 1:
            return 1

        if n == 2:
            return 1

        # 1. 确定数组及下标含义
        # dp: 存放第i个tribonacci的值
        dp = [0] * (n + 1)

        # 2. 确定递推公式
        # dp[i+3] = dp[i] + dp[i+1] + dp[i+2]
        # dp[i] = dp[i-1] + dp[i-2] + dp[i-3]

        # 3. dp数组如何初始化
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1

        # 4. 确定遍历顺序
        # 后项依赖前项，顺序遍历
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

        return dp[n]


if __name__ == '__main__':
    s = Solution()
    print(s.tribonacci(1))

