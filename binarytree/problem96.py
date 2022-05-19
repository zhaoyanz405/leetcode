"""
给你一个整数 n ，求恰由 n 个节点组成且节点值从 1 到 n 互不相同的 二叉搜索树 有多少种？返回满足题意的二叉搜索树的种数。
"""


class Solution:
    def __init__(self):
        self.memo = None

    def numTrees(self, n: int) -> int:
        self.memo = [[0] * n for _ in range(n)]
        return self.count(1, n)

    def count(self, lo, hi):
        """
        闭区间[lo, hi]的数字能够组成的count(lo, hi)种BST
        :param lo:
        :param hi:
        :return:
        """
        if lo > hi:
            return 1

        if self.memo[lo][hi]:
            return self.memo[lo][hi]

        res = 0
        for i in range(lo, hi + 1):
            left = self.count(lo, i - 1)
            right = self.count(i + 1, hi)
            res += left * right

        self.memo[lo][hi] = res

        return res
