class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # 定义dp[i][j]为字符串s[i:j]上的最长回文子序列的长度
        dp = [[0] * len(s) for _ in range(len(s))]
        # 初始化， if i == j, dp[i][j] = 1, if i > j, dp[i][j] = 0
        for i in range(len(s)):
            dp[i][i] = 1

        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(
                        dp[i + 1][j],
                        dp[i][j - 1],
                    )

        return dp[0][-1]
