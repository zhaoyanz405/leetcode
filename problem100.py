from treenode import TreeNode


class Solution:
    def isSameTree(self, p, q) -> bool:
        if p == q:
            return True

        if p != q:
            if p is None or q is None:
                return False

        if p.val != q.val:
            return False

        left_res = self.isSameTree(p.left, q.left)
        if not left_res:
            return False

        right_res = self.isSameTree(p.right, q.right)
        if not right_res:
            return False

        return True


if __name__ == '__main__':
    n2 = TreeNode(2)
    n3 = TreeNode(3)

    n1 = TreeNode(1, n2, None)

    m2 = TreeNode(2)
    m3 = TreeNode(3)

    m1 = TreeNode(1, None, m2)

    s = Solution()
    print(s.isSameTree(n1, m1))
