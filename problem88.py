"""
给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。

请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。

注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。

 

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
解释：需要合并 [1,2,3] 和 [2,5,6] 。
合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/merge-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def merge(self, nums1: list, m: int, nums2: list, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = 0
        p2 = 0

        sortedlist = []

        while p1 < m and p2 < n:
            if nums1[p1] <= nums2[p2]:
                sortedlist.append(nums1[p1])
                p1 += 1
            else:
                sortedlist.append(nums2[p2])
                p2 += 1

        while p1 < m:
            sortedlist.append(nums1[p1])
            p1 += 1

        while p2 < n:
            sortedlist.append(nums2[p2])
            p2 += 1

        nums1[:] = sortedlist


if __name__ == '__main__':
    s = Solution()
    nums1 = [0]
    len_nums1 = len(nums1)
    nums2 = [1]
    len_nums2 = len(nums2)

    nums1 += len_nums2 * [0]
    s.merge(nums1, len_nums1, nums2, len_nums2)
    print(nums1)
