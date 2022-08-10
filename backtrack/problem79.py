class Solution:
    def exist(self, board: list, word: str) -> bool:
        for row in range(len(board)):
            for col in range(len(board[0])):
                used = [[False] * len(board[0]) for _ in board]
                isexist = self.backtrack(board, word, row, col, used, [])
                if isexist:
                    return True
        return False

    def backtrack(self, board, word, row, col, used, path):
        if len(word) == len(path):
            return True

        if row >= len(used) or col >= len(used[0]) or used[row][col]:
            return False

        print(row, col)
        c = board[row][col]
        if word[len(path)] != c:
            # unmatched
            used[row][col] = False
            return False
        else:
            path.append(c)
            used[row][col] = True

        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        res = False
        for x, y in dirs:
            res |= self.backtrack(board, word, row + x, col + y, used, path)

        return res


if __name__ == '__main__':
    s = Solution()
    print(s.exist([["a", "b"], ["c", "d"]],
                  "abcd"))
