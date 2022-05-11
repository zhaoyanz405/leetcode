"""
实现RandomizedSet 类：

RandomizedSet() 初始化 RandomizedSet 对象
bool insert(int val) 当元素 val 不存在时，向集合中插入该项，并返回 true ；否则，返回 false 。
bool remove(int val) 当元素 val 存在时，从集合中移除该项，并返回 true ；否则，返回 false 。
int getRandom() 随机返回现有集合中的一项（测试用例保证调用此方法时集合中至少存在一个元素）。每个元素应该有 相同的概率 被返回。
你必须实现类的所有函数，并满足每个函数的 平均 时间复杂度为 O(1) 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/insert-delete-getrandom-o1
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from random import choice


class RandomizedSet:

    def __init__(self):
        self.store = []
        self._map = {}

    def insert(self, val: int) -> bool:
        if val in self._map:
            return False

        self.store.append(val)
        self._map[val] = len(self.store) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self._map:
            return False

        idx = self._map[val]
        del self._map[val]

        last = self.store.pop()
        if idx <= len(self.store) - 1:
            self.store[idx] = last
            self._map[last] = idx

        return True

    def getRandom(self) -> int:
        return choice(self.store)


if __name__ == '__main__':
    s = RandomizedSet()
    print(s.insert(0))
    print(s.insert(1))
    print(s.remove(0))
    print(s.insert(2))
    print(s.remove(1))
    print(s.getRandom())
