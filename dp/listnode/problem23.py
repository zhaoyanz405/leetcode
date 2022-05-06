"""
合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
from dp.listnode import ListNode, create_listnode


class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        if len(lists) == 2:
            return self.mergeTwoLists(*lists)

        mid = len(lists) // 2
        left = self.mergeKLists(lists[0:mid])
        right = self.mergeKLists(lists[mid:])
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, list1, list2):
        head = ListNode(float('-inf'))
        cur = head

        while list1 and list2:
            if list1.val > list2.val:
                list1, list2 = list2, list1

            cur.next = ListNode(list1.val)
            cur = cur.next
            list1 = list1.next

        cur.next = list1 or list2

        return head.next


if __name__ == '__main__':
    s = Solution()
    s.mergeKLists([
        create_listnode([1, 4, 5]),
        create_listnode([1, 3, 4]),
        create_listnode([2, 6])
    ]).print()
    print(s.mergeKLists([]))
    print(s.mergeKLists([[]]))
