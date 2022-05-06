"""
合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。
"""
from queue import PriorityQueue

from dp.listnode import ListNode, create_listnode


class NListNode(ListNode):

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists):
        head = NListNode(float('-inf'))
        cur = head

        queue = PriorityQueue()
        for ln in lists:
            queue.put(NListNode(ln))

        while not queue.empty():
            min_node = queue.get()
            cur.next = ListNode(min_node.val)
            cur = cur.next

            if min_node.next:
                queue.put(NListNode(min_node.next))

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
