from listnode import ListNode


def is_loop(head: ListNode):
    fast = head
    slow = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # 相遇了
            return True

    return False


def t_is_loop():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n1.next = n2
    n2.next = n3
    n3.next = n2
    print(is_loop(n1))


def find_loop_node(head: ListNode):
    slow = head
    fast = head

    has_loop = False
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # meet
            has_loop = True
            break

    if not has_loop:
        return None

    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return slow


def t_find_loop():
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n1
    print(find_loop_node(n1))


if __name__ == '__main__':
    t_find_loop()
