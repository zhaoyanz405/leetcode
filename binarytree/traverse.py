def traverse_array(arr, i):
    if i == len(arr):
        return

    # 前序
    traverse_array(arr, i + 1)
    # 后序
    print(arr[i])


if __name__ == '__main__':
    traverse_array([1, 2, 3, 4, 5], 0)
