from queue import PriorityQueue


class State:
    def __init__(self, id, dist_from_start):
        self.id = id
        self.dist_from_start = dist_from_start

    def __lt__(self, other):
        return self.dist_from_start - other.dist_from_start < 0

    def __eq__(self, other):
        return self.dist_from_start == other.dist_from_start


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def weight(self, from_, to):
        return self.graph[from_][to]

    def adj(self, id) -> list:
        neibors = []
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for d in dirs:
            nx = id[0] + d[0]
            ny = id[1] + d[1]
            if nx < 0 or ny < 0 or nx >= len(self.graph) or ny >= len(self.graph[0]):
                continue

            neibors.append((nx, ny))

        return neibors

    def dijkstra(self, start):
        dist_to = {}
        dist_to[start] = 0

        pg = PriorityQueue()
        pg.put(State(start, 0))

        while not pg.empty():
            cur_state = pg.get()
            if cur_state.id[0] == len(self.graph) - 1 and cur_state.id[1] == len(self.graph[0]) - 1:
                return cur_state.dist_from_start

            if cur_state.dist_from_start > dist_to[cur_state.id]:
                # 已经有更大的了，不更新
                continue

            for next_id in self.adj(cur_state.id):
                dist_next = max(dist_to[cur_state.id],
                                abs(self.graph[cur_state.id[0]][cur_state.id[1]] - self.graph[next_id[0]][next_id[1]]))
                if next_id not in dist_to or dist_to[next_id] > dist_next:
                    # 更新最小路径
                    dist_to[next_id] = dist_next
                    pg.put(State(next_id, dist_next))

        return -1


class Solution:
    def minimumEffortPath(self, heights: list) -> int:
        dij = Dijkstra(heights)
        return dij.dijkstra((0, 0))


if __name__ == '__main__':
    print(Solution().minimumEffortPath([[1, 2, 3], [3, 8, 4], [5, 3, 5]]))
