import re


class Solution:
    def solveEquation(self, equation: str) -> str:
        inf = "Infinite solutions"
        none = "No solution"
        left, right = equation.split("=")
        if not left or not right:
            return inf

        pattern = re.compile("[+|-]?[x0-9]+")

        left = re.findall(pattern, left)
        right = re.findall(pattern, right)

        xs = 0
        value = 0
        for n in left:
            if n[-1] != 'x':
                value -= self.int(n)
            else:
                xs += self.int(n[:-1])

        for n in right:
            if n[-1] != 'x':
                value += self.int(n)
            else:
                xs -= self.int(n[:-1])

        if xs == 0:
            if value == 0:
                return inf

            return none

        return "x=%s" % int(value / xs)

    def int(self, n):
        if not n:
            return 1

        v = n[1:]
        if n[0] == '-':
            if not v:
                return -1

            return -int(v)

        if n[0] == '+':
            if not v:
                return 1

            return int(v)

        return int(n)


if __name__ == '__main__':
    s = Solution()
    print(s.solveEquation("2x+0=0"))
