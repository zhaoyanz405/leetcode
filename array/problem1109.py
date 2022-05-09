"""
这里有n个航班，它们分别从 1 到 n 进行编号。

有一份航班预订表bookings ，表中第i条预订记录bookings[i] = [firsti, lasti, seatsi]意味着在从 firsti到 lasti （包含 firsti 和 lasti ）的 每个航班 上预订了 seatsi个座位。

请你返回一个长度为 n 的数组answer，里面的元素是每个航班预定的座位总数。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/corporate-flight-bookings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def corpFlightBookings(self, bookings, n: int) -> list:
        diff = [0] * n
        for i, j, k in bookings:
            diff[i - 1] += k
            if j < len(diff):
                diff[j] -= k

        nums = [0] * n
        nums[0] = diff[0]
        for i in range(1, len(diff)):
            nums[i] = nums[i - 1] + diff[i]

        return nums


if __name__ == '__main__':
    s = Solution()
    answers = s.corpFlightBookings(
        bookings=[[1, 2, 10], [2, 3, 20], [2, 5, 25]],
        n=5
    )
    print(answers)
