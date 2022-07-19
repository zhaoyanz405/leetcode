class Solution:
    def dailyTemperatures(self, temperatures: list) -> list:
        stack = []
        res = [0] * len(temperatures)

        for i in range(len(temperatures) - 1, -1, -1):
            while len(stack) and stack[-1]['value'] <= temperatures[i]:
                stack.pop()

            res[i] = 0 if len(stack) == 0 else (stack[-1]['index'] - i)
            stack.append({'value': temperatures[i], 'index': i})

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]))
