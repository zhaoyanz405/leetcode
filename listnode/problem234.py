"""
回文链表

给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。
"""
from listnode import ListNode, create_listnode


class Solution:
    def isPalindrome(self, head: ListNode):
        slow = head
        fast = head

        half = [slow]
        while fast.next and fast.next.next:
            slow = slow.next
            half.append(slow)

            fast = fast.next.next

        if fast and fast.next:
            # 偶数
            slow = slow.next

        while slow:
            if slow.val != half.pop().val:
                return False

            slow = slow.next

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(create_listnode([1, 2, 3, 4, 5])))
    print(s.isPalindrome(create_listnode([1, 2, 3, 2, 1])))
    print(s.isPalindrome(create_listnode([1, 2, 2, 1])))
