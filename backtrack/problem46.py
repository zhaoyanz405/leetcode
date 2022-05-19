import copy


class Solution:
    def __init__(self) -> None:
        self.res = []

    def permute(self, nums: list) -> list:
        track = []
        used = [False] * len(nums)
        self.backtrack(nums, track, used)
        return self.res

    def backtrack(self, nums, track, used):
        if len(track) == len(nums):
            self.res.append(copy.deepcopy(track))
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            track.append(nums[i])
            used[i] = True
            self.backtrack(nums, track, used)
            track.pop()
            used[i] = False


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
