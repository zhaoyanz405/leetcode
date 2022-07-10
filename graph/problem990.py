from graph.uf import UnionFind


class Solution:
    def equationsPossible(self, equations: list) -> bool:
        uf = UnionFind(26)

        not_equals = []
        for expr in equations:
            if expr[1:3] == "==":
                uf.union(self.convert_to_int(expr[0]), self.convert_to_int(expr[-1]))
            else:
                not_equals.append(expr)

        for expr in not_equals:
            if uf.connected(self.convert_to_int(expr[0]), self.convert_to_int(expr[-1])):
                return False

        return True

    def convert_to_int(self, alp):
        return ord(alp) - 97


if __name__ == '__main__':
    print(Solution().equationsPossible(["c==c","b==d","x!=z"]))
