def print_matrix(m):
    for row in m:
        print(row)


def rotate_matrix(matrix):
    """
    将二维矩阵顺时针转动90度
    :param matrix:
    :return:
    """

    # 1. 将矩阵对折
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # 2. 将每一行反转
    for idx in range(len(matrix)):
        matrix[idx].reverse()


if __name__ == '__main__':
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_matrix(test_matrix)
    print_matrix(test_matrix)
