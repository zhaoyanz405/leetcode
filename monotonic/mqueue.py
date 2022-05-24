class DoubleNode:
    def __init__(self, val=None, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

    def is_empty(self):
        pass

    def __str__(self):
        return str(self.val)

    def __repr__(self):
        return self.__str__()


class MonotonicQueue:

    def __init__(self):
        self.dummy = DoubleNode(float('inf'))

    def push(self, value):
        point = self.dummy
        while point.next:
            if point.next.val < value:
                break
            else:
                point = point.next

        n = DoubleNode(value)
        point.next = n
        n.prev = point

    def pop(self, n=None):
        head = self.dummy.next
        if head and head.val != n:
            return

        if head.next:
            head.next.prev = self.dummy

        head.prev.next = head.next

    def max(self):
        # 队列头的元素最大
        if self.dummy.next:
            return self.dummy.next.val

    def __str__(self):
        p = self.dummy.next
        res = []
        while p:
            res.append(p.val)
            p = p.next

        return '->'.join(map(str, res))

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    mq = MonotonicQueue()
    for i, n in enumerate([1, 3, -1, -3, 5, 3, 6, 7]):
        if i < 2:
            mq.push(n)
            print(mq)
        else:
            mq.push(n)
            print('max', mq.max())
            mq.pop()
            print('mq', mq)
