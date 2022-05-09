class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        cur = self
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next

        return "ListNode{%s}" % '->'.join(str(x) for x in res)

    def print(self):
        print(str(self))


def create_listnode(xlist):
    head, cur = None, None
    for x in xlist:
        if head is None:
            head = ListNode(x)
            cur = head
        else:
            cur.next = ListNode(x)
            cur = cur.next

    return head


if __name__ == '__main__':
    n = create_listnode([1, 2, 3])
    n.print()
