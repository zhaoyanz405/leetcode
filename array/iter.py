def print_matrix(m):
    for row in m:
        print(row)


def rotate_matrix_cw(matrix):
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


def rotate_matrix_ccw(matrix):
    """
    逆时针旋转矩阵90度
    :param matrix:
    :return:
    """
    n = len(matrix)
    # 1. 对折
    for i in range(n):
        for j in range(n - i):
            matrix[i][j], matrix[n - 1 - j][n - 1 - i] = matrix[n - 1 - j][n - 1 - i], matrix[i][j]

    for idx in range(n):
        matrix[idx].reverse()


if __name__ == '__main__':
    test_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_matrix_ccw(test_matrix)
    print_matrix(test_matrix)
