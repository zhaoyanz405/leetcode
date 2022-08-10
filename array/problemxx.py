class Solution:
    def findPairs(self, nums: list, k: int) -> int:
        # 1.跳过自身，二相同的元祖只保留一个
        mapping = {}
        for i, n in enumerate(nums):
            if n not in mapping:
                mapping[n] = []

            mapping[n].append(i)

        def match(i, target):
            if target in mapping:
                for j in mapping[target]:
                    if i == j:
                        continue

                    n1, n2 = nums[i], nums[j]
                    if n1 > n2:
                        n1, n2 = n2, n1

                    res.add((n1, n2))

        res = set()
        for i, n in enumerate(nums):
            if n - k == k - n == n:
                continue

            match(i, n - k)
            match(i, k - n)

        return len(res)


if __name__ == '__main__':
    s = Solution()
    print(s.findPairs([1, 3, 1, 5, 4], 0))
