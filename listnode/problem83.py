"""
83. 删除排序链表中的重复元素

给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。
"""
from listnode import ListNode, create_listnode


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next
            if slow.val != fast.val:
                slow = slow.next
                slow.val = fast.val

        if slow:
            slow.next = None

        return head


if __name__ == '__main__':
    s = Solution()
    s.deleteDuplicates(create_listnode([0, 0, 1, 1, 1, 1, 2, 2, 3, 3, 4, 4, 5, 6])).print()
