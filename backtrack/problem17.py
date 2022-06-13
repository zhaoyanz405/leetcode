class Solution:
    def __init__(self):
        self.res = []
        self.map = {
            '1': "",
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str) -> list:
        if not digits:
            return []

        self.backtrack([], digits, 0)
        return self.res

    def backtrack(self, path, digits, start):
        if len(path) == len(digits):
            self.res.append(''.join(path))
            return

        for i in range(start, len(digits)):
            d = digits[i]
            for c in self.map[d]:
                path.append(c)
                self.backtrack(path, digits, i + 1)
                path.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations('23'))
