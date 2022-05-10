"""
给定两个字符串s和 p，找到s中所有p的异位词的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

异位词 指由相同字母重排列形成的字符串（包括相同的字符串）。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-all-anagrams-in-a-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list:
        answers = []

        needs = {c: p.count(c) for c in p}
        window = {}

        left = 0
        right = 0
        start = 0
        valid = 0

        while right < len(s):
            cur = s[right]
            right += 1

            if cur in needs:
                if cur not in window:
                    window[cur] = 0

                window[cur] += 1
                if window[cur] == needs[cur]:
                    valid += 1

            while right - left >= len(p):
                if valid == len(needs):
                    answers.append(left)

                d = s[left]
                left += 1
                if d in window:
                    if window[d] == needs[d]:
                        valid -= 1
                    window[d] -= 1

        return answers


if __name__ == '__main__':
    s = Solution()
    print(s.findAnagrams(s="cbaebabacd", p="abc"))
    print(s.findAnagrams(s="abab", p="ab"))
    print(s.findAnagrams(s="baa", p="aa"))
