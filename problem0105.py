"""
字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
"""


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        if len(first) < len(second):
            first, second = second, first

        if len(first) - len(second) > 1:
            return False

        op_times = 0
        if len(first) == len(second):
            # 只能通过删除来操作
            for a, b in zip(first, second):
                if a != b:
                    op_times += 1
                    if op_times > 1:
                        return False

        else:
            # 只能通过插入来操作
            point_f = 0
            point_s = 0

            # 尝试从左向右走，必定会遇到不一致的情况
            while point_s < len(second):
                if second[point_s] == first[point_f]:
                    point_s += 1
                    point_f += 1
                else:
                    point_f += 1
                    op_times += 1

                if op_times > 1:
                    return False

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.oneEditAway("intention", "execution"))
