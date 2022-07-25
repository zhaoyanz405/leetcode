from queue import Queue


class State:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __lt__(self, other):
        return self.value - other.value < 0

    def __eq__(self, other):
        return self.value == other.value


class Dijkstra:

    def __init__(self, graph, dirs):
        self.graph = graph
        self.dirs = dirs
        self.path = {}

    def weight(self, s):
        return self.graph[s[0]][s[1]]

    def adj(self, s) -> list:
        neibors = []

        for d in self.dirs:
            nx = s[0] + d[0]
            ny = s[1] + d[1]

            if nx < 0 or ny < 0 or nx >= len(self.graph) or ny >= len(self.graph[0]):
                continue

            if self.graph[nx][ny] != -1:
                neibors.append((nx, ny))

        return neibors

    def dijkstra(self, start, end):
        vals_to = {start: self.weight(start)}
        self.path[(0, 0)] = None

        pg = Queue()
        pg.put(State(start, 0))

        while not pg.empty():
            cur_state = pg.get()

            if cur_state.id[0] == end[0] and cur_state.id[1] == end[1]:
                continue

            if cur_state.value < vals_to[cur_state.id]:
                # 当前值太小了，不更新
                continue

            for next_id in self.adj(cur_state.id):
                val_next = vals_to[cur_state.id] + self.graph[next_id[0]][next_id[1]]
                if next_id not in vals_to or vals_to[next_id] < val_next:
                    vals_to[next_id] = val_next
                    self.path[next_id] = cur_state.id
                    pg.put(State(next_id, val_next))

        return vals_to[end]


class Solution:
    def cherryPickup(self, grid: list) -> int:
        d = Dijkstra(grid, [(0, 1), (1, 0)])


if __name__ == '__main__':
    data = [
        [1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 1],
        [1, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1]
    ]
    m, n = len(data) - 1, len(data[0]) - 1
    d = Dijkstra(data, [(0, 1), (1, 0)])
    print(d.dijkstra(start=(0, 0), end=(m, n)))

    p = (m, n)
    while p:
        print(p)
        data[p[0]][p[1]] = 0
        p = d.path[p]

    for row in data:
        print(row)

    d2 = Dijkstra(data, [(0, 1), (1, 0)])
    print(d.dijkstra(start=(0, 0), end=(m, n)))
    # todo it is not perfect
