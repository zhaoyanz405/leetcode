class Solution:
    def kSmallestPairs(self, nums1: list, nums2: list, k: int) -> list:
        res = []
        p1 = p2 = 0

        i = 0
        while i < k:
            i += 1
            res.append((nums1[p1], nums2[p2]))
            # p1走一步
            if p1 >= len(nums1) - 1:
                break

            p1sum = nums1[p1 + 1] + nums2[p2]

            # p2走一步
            if p2 >= len(nums2) - 1:
                p2sum = float('inf')
            else:
                p2sum = nums1[p1] + nums2[p2 + 1]

            # 判断该向哪里走
            if p1sum <= p2sum:
                p1 += 1
                p2 = 0
            else:
                p2 += 1

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.kSmallestPairs([1, 1, 2],
                           [1, 2, 3],
                           10))
