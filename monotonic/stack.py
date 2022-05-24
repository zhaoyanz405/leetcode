def next_greater_element(nums):
    res = [0] * len(nums)
    stack = []
    for i in range(len(nums) - 1, -1, -1):
        while len(stack) and stack[-1] <= nums[i]:
            stack.pop()

        res[i] = -1 if len(stack) == 0 else stack[-1]
        stack.append(nums[i])

    return res


if __name__ == '__main__':
    print(next_greater_element([2, 1, 2, 4, 3]))
