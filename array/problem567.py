"""
给你两个字符串s1和s2 ，写一个函数来判断 s2 是否包含 s1的排列。如果是，返回 true ；否则，返回 false 。

换句话说，s1 的排列之一是 s2 的 子串 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/permutation-in-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        window = {}
        needs = {}
        for c in s1:
            if c not in needs:
                needs[c] = 0
            needs[c] += 1

        left = right = 0
        valid = 0
        length = float('inf')
        start = 0

        while right < len(s2):
            current_char = s2[right]
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
                c = s2[left]
                left += 1

                if c in needs:
                    if window[c] == needs[c]:
                        valid -= 1

                    window[c] -= 1

        print(s2[start: start + length])
        return length == len(s1)


if __name__ == '__main__':
    s = Solution()
    print(s.checkInclusion(s1="ab", s2="eidbaooo"))
    print(s.checkInclusion(s1="ab", s2="eidboaoo"))
