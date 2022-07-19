from listnode import ListNode, create_listnode


class Solution:
    def sortList(self, head):
        if not head:
            return

        if not head.next:
            return head

        slow = head
        fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        n1 = head
        n2 = slow.next
        slow.next = None

        first = self.sortList(n1)
        second = self.sortList(n2)
        return self.merge(first, second)

    def merge(self, n1, n2):
        p1 = n1
        p2 = n2

        dummy = ListNode(-1)
        p = dummy

        while p1 and p2:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
            else:
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
    s.sortList(create_listnode([4, 2, 1, 3])).print()
