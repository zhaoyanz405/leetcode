def findMaxProducts(products):
    # Write your code here
    maxsize = 0
    # 定义dp[i] = products[:i+1]的最大值
    dp = [0] * len(products)
    dp[0] = products[0]

    for i in range(1, len(products)):
        if products[i] > products[i - 1]:
            dp[i] = dp[i - 1] + products[i]
        elif products[i] <= products[i - 1]:
            choices = [products[i]]
            for j in range(i - 1, -1, -1):
                if products[j] < choices[-1]:
                    choices.append(products[j])
                else:
                    v = choices[-1] - 1
                    if v > 0:
                        choices.append(v)
                    else:
                        break
            dp[i] = sum(choices)

        maxsize = max(maxsize, dp[i])

    return maxsize


if __name__ == '__main__':
    print(findMaxProducts([2, 0, 10000]))
