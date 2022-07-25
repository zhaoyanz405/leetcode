"""
给定链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""
from listnode import ListNode, create_listnode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head:
            return

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        if not head2:
            return head

        slow.next = None

        left = self.sortList(head)
        right = self.sortList(head2)

        return self.merge(left, right)

    def merge(self, left, right):
        if not left and not right:
            return

        if not left:
            return right

        if not right:
            return left

        p1 = left
        p2 = right
        dummy = ListNode(-1)
        p = dummy
        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            elif p1.val >= p2.val:
                p.next = p2
                p2 = p2.next

            p = p.next

        if p1:
            p.next = p1

        if p2:
            p.next = p2

        return dummy.next


if __name__ == '__main__':
    s = Solution()
    s.sortList(create_listnode([3, 2, 1, 5, 4, 6, 9, 4, 2, 4, 1, 0])).print()
