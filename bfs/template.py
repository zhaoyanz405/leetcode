from queue import Queue


def bfs(start, target):
    q = Queue()
    visited = {}

    q.put(start)
    visited[start] = True

    step = 0
    while not q.empty():
        sz = q.qsize()
        for i in range(sz):
            cur = q.get()
            if cur is target:
                return step

            for n in cur.around():
                if n not in visited:
                    q.put(n)
                    visited[n] = True

        step += 1
