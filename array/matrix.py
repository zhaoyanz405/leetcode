def spiral_copy(inputMatrix):
    to_right = True
    to_top = to_left = to_bottom = False

    top = left = 0
    bottom = len(inputMatrix)
    right = len(inputMatrix[0])

    res = []
    while left < right and top < bottom:
        if to_right:
            for idx in range(left, right):
                res.append(inputMatrix[top][idx])

            to_right = False
            to_bottom = True
            top += 1
            continue

        if to_bottom:
            for idx in range(top, bottom):
                res.append(inputMatrix[idx][right - 1])

            to_bottom = False
            to_left = True
            right -= 1
            continue

        if to_left:
            for idx in range(right - 1, left - 1, -1):
                res.append(inputMatrix[bottom - 1][idx])

            to_left = False
            to_top = True
            bottom -= 1
            continue

        if to_top:
            for idx in range(bottom - 1, top - 1, -1):
                res.append(inputMatrix[idx][left])

            to_top = False
            to_right = True
            left += 1
            continue

    return res


if __name__ == '__main__':
    matrix = [[1, 2]]

    print(spiral_copy(matrix))
