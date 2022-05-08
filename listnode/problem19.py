"""
删除链表的倒数第 N 个结点
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
"""
from listnode import ListNode


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(-1)
        dummy.next = head

        p1 = head
        p2 = dummy
        for i in range(n):
            p1 = p1.next

        while p1:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next
        return dummy.next


if __name__ == '__main__':
    s = Solution()
    s.removeNthFromEnd(ListNode(1), 1).print()
