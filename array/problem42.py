class Solution:
    def trap(self, height: list) -> int:
        if len(height) < 3:
            return 0

        highest_left = [0] * len(height)
        highest_left[0] = height[0]

        highest_right = [0] * len(height)
        highest_right[-1] = height[-1]

        for i in range(1, len(height)):
            highest_left[i] = max(height[i], highest_left[i - 1])

        for i in range(len(height) - 2, -1, -1):
            highest_right[i] = max(height[i], highest_right[i + 1])

        res = 0
        for i in range(1, len(height) - 1):
            res += min(
                highest_left[i],
                highest_right[i]
            ) - height[i]

        return res

    def trap2(self, height):
        res = 0
        stack = list()

        for i, h in enumerate(height):
            while stack and h > height[stack[-1]]:
                idx = stack.pop()
                if not stack:
                    break

                left = stack[-1]
                cur_width = i - left - 1
                cur_height = min(height[left], height[i]) - height[idx]
                res += cur_width * cur_height

            stack.append(i)

        return res

    def trap3(self, height):
        res = 0
        left, right = 0, len(height) - 1
        left_max = right_max = 0

        while left < right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            if height[left] < height[right]:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1

        return res



if __name__ == '__main__':
    s = Solution()
    print(s.trap3([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
