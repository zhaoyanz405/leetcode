"""
你有一个带有四个圆形拨轮的转盘锁。每个拨轮都有10个数字： '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' 。每个拨轮可以自由旋转：例如把 '9' 变为 '0'，'0' 变为 '9' 。每次旋转都只能旋转一个拨轮的一位数字。

锁的初始数字为 '0000' ，一个代表四个拨轮的数字的字符串。

列表 deadends 包含了一组死亡数字，一旦拨轮的数字和列表里的任何一个元素相同，这个锁将会被永久锁定，无法再被旋转。

字符串 target 代表可以解锁的数字，你需要给出解锁需要的最小旋转次数，如果无论如何不能解锁，返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/open-the-lock
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def openLock(self, deadends: list, target: str) -> int:
        # '0000' -> target
        from queue import Queue
        q = Queue()
        q.put('0000')
        visited = {}
        deads = {}
        for d in deadends:
            deads[d] = True

        step = 0
        while not q.empty():
            sz = q.qsize()
            for i in range(sz):
                cur = q.get()
                if cur in deads:
                    continue

                if cur == target:
                    return step

                for j in range(4):
                    choice = [self.plus_one(cur, j), self.minus_one(cur, j)]
                    for c in choice:
                        if c not in visited:
                            q.put(c)
                            visited[c] = True

            step += 1

        return -1

    def plus_one(self, s: str, index: int) -> str:
        s = list(s)
        if s[index] == '9':
            s[index] = '0'
        else:
            s[index] = str(int(s[index]) + 1)

        return ''.join(s)

    def minus_one(self, s: str, index: int) -> str:
        s = list(s)
        if s[index] == '0':
            s[index] = '9'
        else:
            s[index] = str(int(s[index]) - 1)

        return ''.join(s)


if __name__ == '__main__':
    s = Solution()
    print(s.openLock(deadends=["8887","8889","8878","8898","8788","8988","7888","9888"], target="8888"))
