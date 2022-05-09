"""
反转链表 II

给你单链表的头指针 head 和两个整数left 和 right ，其中left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from listnode import ListNode, create_listnode


class Solution:
    successor = None

    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == 1:
            return self.reverseN(head, right)
        else:
            head.next = self.reverseBetween(head.next, left - 1, right - 1)
        return head

    def reverseN(self, head, n):
        """
        反转前n个节点
        :param head:
        :param n:
        :return:
        """
        if n == 1:
            self.successor = head.next
            return head

        last = self.reverseN(head.next, n - 1)
        head.next.next = head
        head.next = self.successor
        return last


if __name__ == '__main__':
    s = Solution()
    s.reverseN(create_listnode([1, 2, 3, 4, 5]), 3).print()
    s.reverseBetween(create_listnode([1, 2, 3, 4, 5]), 2, 4).print()
