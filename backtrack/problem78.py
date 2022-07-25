import copy


from collections import deque
class Solution:
    def __init__(self):
        self.res = []

    def subsets(self, nums: list) -> list:
        track = []
        self.backtrack(nums, track, 0)
        return self.res

    def backtrack(self, nums, track, start):
        self.res.append(copy.deepcopy(track))
        for i in range(start, len(nums)):
            track.append(nums[i])
            self.backtrack(nums, track, start + 1)
            track.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2, 3]))
