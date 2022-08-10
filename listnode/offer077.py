"""
给定链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。
"""
from listnode import ListNode, create_listnode


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        head, _ = self.sort(head)
        return head

    def sort(self, head):
        if not head:
            return None, None

        # 以第一个节点做划分，快排
        left = ListNode(-1)
        pleft = left

        done = ListNode(-1)
        pdone = done

        right = ListNode(-1)
        pright = right

        p = head
        while p:
            if p.val == head.val:
                pdone.next = p
                p = p.next

                pdone = pdone.next
                pdone.next = None
            elif p.val < head.val:
                pleft.next = p
                p = p.next

                pleft = pleft.next
                pleft.next = None
            elif p.val > head.val:
                pright.next = p
                p = p.next

                pright = pright.next
                pright.next = None

        left, last_left = self.sort(left.next)
        right, last_right = self.sort(right.next)

        dummy = ListNode(-1)
        point = dummy
        if left:
            point.next = left
            point = last_left

        if done:
            point.next = done.next
            point = pdone

        if right:
            point.next = right
            point = last_right

        return dummy.next, point


if __name__ == '__main__':
    s = Solution()
    s.sortList(create_listnode([3, 2, 1, 5, 4, 6, 9, 4, 2, 4, 1, 0])).print()
