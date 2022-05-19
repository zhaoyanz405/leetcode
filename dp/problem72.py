"""
给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数  。

你可以对一个单词进行如下三种操作：

插入一个字符
删除一个字符
替换一个字符

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/edit-distance
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j]表示word1[0:i],word2[0:j]所需要最小的编辑距离
        dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
        dp[0][0] = 0

        for i in range(1, len(word1) + 1):
            dp[i][0] = i

        for j in range(1, len(word2) + 1):
            dp[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(
                        dp[i][j - 1] + 1,
                        dp[i - 1][j] + 1,
                        dp[i - 1][j - 1] + 1
                    )

        return dp[len(word1)][len(word2)]

    def resolve(self, word1, word2):
        def dp(i, j):
            if i < 0:
                return j + 1

            if j < 0:
                return i + 1

            if word1[i] == word2[j]:
                return dp(i - 1, j - 1)
            else:
                return min(
                    dp(i, j - 1) + 1,  # 插入
                    dp(i - 1, j) + 1,  # 删除
                    dp(i - 1, j - 1) + 1  # 替换
                )

        return dp(len(word1) - 1, len(word2) - 1)


if __name__ == '__main__':
    s = Solution()
    print(s.minDistance(word1="horse", word2="ros"))
    print(s.minDistance(word1="intention", word2="execution"))
