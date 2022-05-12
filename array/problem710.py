"""
给定一个整数 n 和一个 无重复 黑名单整数数组blacklist。设计一种算法，从 [0, n - 1] 范围内的任意整数中选取一个未加入黑名单blacklist的整数。任何在上述范围内且不在黑名单blacklist中的整数都应该有 同等的可能性 被返回。

优化你的算法，使它最小化调用语言 内置 随机函数的次数。

实现Solution类:

Solution(int n, int[] blacklist)初始化整数 n 和被加入黑名单blacklist的整数
int pick()返回一个范围为 [0, n - 1] 且不在黑名单blacklist 中的随机整数

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/random-pick-with-blacklist
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from random import randint


class Solution:

    def __init__(self, n: int, blacklist: list):
        self.blackmap = {}
        self.n = n
        self.blacklist = blacklist

        last = n - 1
        for b in blacklist:
            if b >= n - len(blacklist):
                continue

            while last in blacklist:
                last -= 1

            self.blackmap[b] = last
            last -= 1

    def pick(self) -> int:
        blen = len(self.blacklist)
        x = randint(0, self.n - 1 - blen)
        if x in self.blackmap:
            return self.blackmap[x]

        return x


if __name__ == '__main__':
    s = Solution(3, [2])
    for i in range(10):
        print(s.pick())
