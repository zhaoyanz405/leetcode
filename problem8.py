import math


class Solution:
    def myAtoi(self, s: str) -> int:
        pos = 0
        res = 0

        limit = int(math.pow(2, 31))
        max = limit - 1
        min = -limit

        idx = len(s) - 1
        meet_number = False
        while idx >= 0:
            try:
                n = int(s[idx])
                meet_number = True
                res += int(math.pow(10, pos)) * n
                pos += 1
                idx -= 1
            except:
                if s[idx] == '-':
                    res *= -1
                    break

                idx -= 1
                if meet_number:
                    return 0

                continue

        if res > max:
            return max

        if res < min:
            return min

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.myAtoi("987 words and "))
