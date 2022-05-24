"""
给你一个整数数组 nums，有一个大小为k的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sliding-window-maximum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from monotonic.mqueue import MonotonicQueue


class Solution:
    def maxSlidingWindow(self, nums: list, k: int) -> list:
        mq = MonotonicQueue()

        res = []
        for i in range(len(nums)):
            if i < k - 1:
                mq.push(nums[i])
            else:
                mq.push(nums[i])
                res.append(mq.max())
                mq.pop(nums[i - k + 1])

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.maxSlidingWindow(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3))
