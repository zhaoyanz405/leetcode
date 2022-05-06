class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def print(self):
        cur = self
        res = []
        while cur:
            res.append(cur.val)
            cur = cur.next

        print('->'.join(str(x) for x in res))


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
