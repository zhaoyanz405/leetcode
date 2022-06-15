class Solution:
    def findClosestNumber(self, nums) -> int:
        closet = [float('inf')]
        for n in nums:
            t = abs(n)
            c = abs(closet[0])
            if t < c:
                closet = [n]
            elif t == c:
                closet.append(n)

        return max(closet)


if __name__ == '__main__':
    s = Solution()
    print(s.findClosestNumber([-4, -2, 1, 4, 8]))
