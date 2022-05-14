class Solution:
    def inorderTraversal(self, root):
        res = []
        if root is None:
            return res

        if root.left:
            res += self.inorderTraversal(root.left)

        res.append(root.val)

        if root.right:
            res += self.inorderTraversal(root.right)

        return res
