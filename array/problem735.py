class Solution:
    def asteroidCollision(self, asteroids):
        if not asteroids:
            return

        stack = [asteroids[0]]
        for i in range(1, len(asteroids)):
            p = asteroids[i]
            while p:
                if p < 0:
                    if stack[-1] < 0:
                        stack.append(p)
                        p = None
                    elif stack[-1] > 0:
                        x = abs(stack[-1]) - abs(p)
                        if x > 0:
                            p = None
                        elif x == 0:
                            stack.pop()
                            p = None
                        elif x < 0:
                            stack.pop()

                else:
                    stack.append(p)
                    p = None

        return stack


if __name__ == '__main__':
    print(Solution().asteroidCollision([10, 2, -5]))
    print(Solution().asteroidCollision([-2, -2, 1, -2]))
