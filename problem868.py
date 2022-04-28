"""
给定一个正整数 n，找到并返回 n 的二进制表示中两个 相邻 1 之间的 最长距离 。如果不存在两个相邻的 1，返回 0 。

如果只有 0 将两个 1 分隔开（可能不存在 0 ），则认为这两个 1 彼此 相邻 。两个 1 之间的距离是它们的二进制表示中位置的绝对差。例如，"1001" 中的两个 1 的距离为 3 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/binary-gap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

分析：
整数转二进制，
设n=22，
22/2 = 11     b=0
11/2 = 5      b=1
5/2=2         b=1
2/2=1         b=0
1/2=0         b=1

10进制22=2进制10110
"""


class Solution:
    def binaryGap(self, n: int) -> int:
        start = False
        max_length = 0

        while n:
            p = n % 2

            if not start:
                if p == 0:
                    length = 0
                else:
                    length = 1
                    start = True
            else:
                if p == 0:
                    length += 1
                else:
                    start = False
                    max_length = max(max_length, length)
                    length = 0
                    continue

            n = int(n / 2)

        return max_length

    def comparator(self, n):
        sbin = str(bin(n)[2:]).strip('0').split('1')
        return max(len(s) + 1 for s in sbin)


if __name__ == '__main__':
    s = Solution()
    print(s.binaryGap(8))
    print(s.comparator(8))
