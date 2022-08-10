class Solution:
    def __init__(self):
        self.res = set()

    def generateParenthesis(self, n: int) -> list:
        self.backtrack(n, n, [])
        return list(self.res)

    def backtrack(self, left, right, path):
        if right < left:
            return

        if left < 0 or right < 0:
            return

        if left == 0 and right == 0:
            self.res.add(''.join(path))

        # 0 < left < right < n

        path.append('(')
        self.backtrack(left - 1, right, path)
        path.pop()

        path.append(')')
        self.backtrack(left, right - 1, path)
        path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis(3))
