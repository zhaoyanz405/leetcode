from queue import PriorityQueue


class State:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def __lt__(self, other):
        return self.value - other.value < 0

    def __eq__(self, other):
        return self.value == other.value


class Dijkstra:
    def __init__(self, graph):
        self.graph = graph

    def weight(self, from_, to):
        raise NotImplemented

    def adj(self, s) -> list:
        raise NotImplemented

    def dijkstra(self, start):
        dist_to = [float('inf')] * len(self.graph)
        dist_to[start] = start

        pg = PriorityQueue()
        pg.put(State(start, 0))

        while not pg.empty():
            cur_state = pg.get()

            if cur_state.value > dist_to[cur_state.id]:
                # 已经有更大的了，不更新
                continue

            for next_id in self.adj(cur_state.id):
                dist_next = dist_to[cur_state.id] + self.weight(cur_state.id, next_id)
                if dist_to[next_id] > dist_next:
                    # 更新最小路径
                    dist_to[next_id] = dist_next
                    pg.put(State(next_id, dist_next))

        return dist_to


if __name__ == '__main__':
    s1 = State('a', 1)
    s2 = State('b', 2)
    print(s1 < s2)
    print(s1 == s2)
