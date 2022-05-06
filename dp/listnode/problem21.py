"""
将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。
"""

from dp.listnode import ListNode, create_listnode


class Solution:
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
    s.mergeTwoLists(create_listnode([1, 2, 4]), create_listnode([1, 3, 4])).print()
    s.mergeTwoLists(create_listnode([1, 2, 4]), None).print()
    s.mergeTwoLists(None, create_listnode([1, 3, 4])).print()
