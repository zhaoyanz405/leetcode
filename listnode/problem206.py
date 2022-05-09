"""
反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。
"""
from listnode import ListNode, create_listnode


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        last = self.reverseList(head.next)
        head.next.next = head
        head.next = None

        return last


if __name__ == '__main__':
    s = Solution()
    s.reverseList(create_listnode([1, 2, 3, 4, 5])).print()
