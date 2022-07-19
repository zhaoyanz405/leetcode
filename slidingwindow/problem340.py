"""
给定一个字符串 s ，找出 至多 包含 k 个不同字符的最长子串 T。
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        longest = ''
        need = {}
        window = ''
        left = 0
        right = 0

        while right < len(s):
            c = s[right]
            if c not in need:
                need[c] = 0
            need[c] += 1
            window += c

            while len(need) > k:
                # 从左开始删除，直至len(need)
                lc = s[left]
                need[lc] -= 1
                if need[lc] == 0:
                    del need[lc]

                window = window[1:]
                left += 1

            if len(window) > len(longest):
                longest = window

            right += 1

        return len(longest)


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstringKDistinct(s="eceba", k=2))
    print(s.lengthOfLongestSubstringKDistinct(s="aa", k=1))
    print(s.lengthOfLongestSubstringKDistinct(s="aba", k=1))

