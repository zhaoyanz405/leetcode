class Solution:
    def nextGreaterElement(self, nums1: list, nums2: list) -> list:
        stack = []
        res = {}

        for i in range(len(nums2) - 1, -1, -1):
            while len(stack) and stack[-1] <= nums2[i]:
                stack.pop()

            res[nums2[i]] = -1 if len(stack) == 0 else stack[-1]
            stack.append(nums2[i])

        print(res)
        return [res[n] for n in nums1]


if __name__ == '__main__':
    s = Solution()
    print(s.nextGreaterElement(nums1=[4, 1, 2], nums2=[1, 3, 4, 2]))
