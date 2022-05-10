"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        left = 0
        right = 0
        needs = {}
        length = 1
        while right < len(s):
            cur = s[right]
            right += 1
            if cur not in needs:
                needs[cur] = 0

            needs[cur] += 1

            while needs[cur] > 1:
                length = max(length, len(needs))
                d = s[left]
                left += 1

                needs[d] -= 1
                if needs[d] == 0:
                    del needs[d]

        length = max(length, len(needs))
        return length


if __name__ == '__main__':
    s = Solution()
    print(s.lengthOfLongestSubstring("abcabcbb"))
    print(s.lengthOfLongestSubstring("bbb"))
    print(s.lengthOfLongestSubstring("pwwkew"))
    print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring(""))
    print(s.lengthOfLongestSubstring("ab"))
