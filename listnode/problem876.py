"""
给定一个头结点为 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。
"""
from listnode import ListNode


class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        fast = head
        slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow
