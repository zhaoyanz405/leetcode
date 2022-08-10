"""
移掉K位数字

给你一个以字符串表示的非负整数num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。

示例 1 ：

输入：num = "1432219", k = 3
输出："1219"
解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
示例 2 ：

输入：num = "10200", k = 1
输出："200"
解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
示例 3 ：

输入：num = "10", k = 2
输出："0"
解释：从原数字移除所有的数字，剩余为空就是 0 。

作者：知鱼君
链接：https://juejin.cn/post/6992227789713702948
"""


class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        count = len(num) - k
        if count <= 0:
            return "0"

        res = ""
        p = -1
        for i in range(count):
            n, p = self.findmin(num, p+1, k+1-i)
            res += n

        return res

    def findmin(self, num, start, end):
        print(num[start:end])
        res = float('inf')
        pos = None
        for i, c in enumerate(num[start:end]):
            n = int(c)
            if n < res:
                res = n
                pos = i + start

        return str(res), pos


if __name__ == '__main__':
    test_data = [
        # num,  k, expect
        "", 1, "0",
        "01", 1, "0",
        "10200", 1, "1",
        "1432219", 3, "1219"
    ]

    s = Solution()
    print(s.removeKdigits("1432219",3))
    exit()
    for d in test_data:
        assert s.removeKdigits(d[0], d[1]) == d[2]
