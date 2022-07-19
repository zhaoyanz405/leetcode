from queue import Queue

from binarytree.treenode import TreeNode, create_tree


class Solution:
    def levelOrderBottom(self, root: TreeNode) -> list:
        if not root:
            return []

        res = Queue()
        answers = list()

        res.put(root)
        while not res.empty():
            sz = res.qsize()

            values = []
            for i in range(sz):
                node = res.get()
                values.append(node.val)

                if node.left:
                    res.put(node.left)

                if node.right:
                    res.put(node.right)

            answers.append(values)

        answers.reverse()
        return answers


if __name__ == '__main__':
    s = Solution()
    print(s.levelOrderBottom(create_tree([3, 9, 20, None, None, 15, 7])))
