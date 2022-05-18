"""
给定两个字符串text1 和text2，返回这两个字符串的最长 公共子序列 的长度。如果不存在 公共子序列 ，返回 0 。

一个字符串的子序列是指这样一个新的字符串：它是由原字符串在不改变字符的相对顺序的情况下删除某些字符（也可以不删除任何字符）后组成的新字符串。

例如，"ace" 是 "abcde" 的子序列，但 "aec" 不是 "abcde" 的子序列。
两个字符串的 公共子序列 是这两个字符串所共同拥有的子序列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-common-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # dp[i][j]是text1[:i]和text2[:j]的最长公共子序列长度
        # dp[i][j] = dp[i-1][j-1] + 1, if text1[i] == text2[j]
        #          = max(dp[i-1][j], dp[i][j-1])
        dp = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        # dp的初始化，i和j其中任意一方为0，则公共子序列长度都为0
        for i in range(1, len(text1) + 1):
            for j in range(1, len(text2) + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(
                        dp[i - 1][j],
                        dp[i][j - 1]
                    )

        return dp[len(text1)][len(text2)]


if __name__ == '__main__':
    s = Solution()
    print(s.longestCommonSubsequence(text1="abcde", text2="ace"))
