"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window = {}
        needs = {}
        for c in t:
            if c not in needs:
                needs[c] = 0
            needs[c] += 1

        left = right = 0
        valid = 0
        length = float('inf')
        start = 0

        while right < len(s):
            current_char = s[right]
            right += 1

            if current_char in needs:
                if current_char not in window:
                    window[current_char] = 0
                window[current_char] += 1

                if window[current_char] == needs[current_char]:
                    valid += 1

            while valid == len(needs):
                # 更新最小覆盖字串
                if right - left < length:
                    start = left
                    length = right - left

                # 已经满足条件，开始收缩
                c = s[left]
                left += 1

                if c in needs:
                    if window[c] == needs[c]:
                        valid -= 1

                    window[c] -= 1

        if length == float('inf'):
            return ""

        return s[start: start + length]


if __name__ == '__main__':
    s = Solution()
    print(s.minWindow(s="a", t="a"))
