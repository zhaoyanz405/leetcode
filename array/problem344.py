"""
编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 s 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def reverseString(self, s: list) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

        print(s)


if __name__ == '__main__':
    s = Solution()
    s.reverseString([])
    s.reverseString([1])
    s.reverseString([1, 2, 3, 4])
    s.reverseString([1, 2, 3, 4, 5])
