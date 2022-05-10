"""
给你一个字符串 s，找到 s 中最长的回文子串。
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''

        mstr = ''
        for i in range(len(s)):
            res = self.findPalindrome(s, i, i)
            if len(res) > len(mstr):
                mstr = res

            res = self.findPalindrome(s, i, i + 1)
            if len(res) > len(mstr):
                mstr = res

        return mstr

    def findPalindrome(self, s, l, r):
        """
        查找以s[i]为中心的最长回文串
        """
        while l >= 0 and r < len(s):
            if s[l] != s[r]:
                break

            l -= 1
            r += 1

        return s[l + 1:r]


if __name__ == '__main__':
    s = Solution()
    print(s.longestPalindrome('aba'))
    print(s.longestPalindrome('abab'))
    print(s.longestPalindrome('ababcca'))
    print(s.longestPalindrome('cbabaca'))
    print(s.longestPalindrome('cbabbaca'))
