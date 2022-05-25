class Solution:
    def diffWaysToCompute(self, expression: str) -> list:
        if not expression:
            return [0]

        res = []
        for i in range(len(expression)):
            if expression[i] in ['-', '*', '+']:
                left = self.diffWaysToCompute(expression[:i])
                right = self.diffWaysToCompute(expression[i + 1:])
                for nl in left:
                    for nr in right:
                        res.append(eval(f"{nl}{expression[i]}{nr}"))

        if len(res) == 0:
            res.append(int(expression))

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.diffWaysToCompute("2-1-1"))
