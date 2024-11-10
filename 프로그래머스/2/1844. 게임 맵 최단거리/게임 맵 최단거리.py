from collections import deque

def solution(maps):
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    N = len(maps)
    M = len(maps[0])
    queue = deque([(0, 0, 1)])
    maps[0][0] = 0
    while queue:
        x, y, step = queue.popleft()
        if x == N-1 and y == M-1: return step

        for elem in d:
            dx, dy = x + elem[0], y + elem[1]
            if not (0 <= dx < N) or not (0 <= dy < M):
                continue
            if not maps[dx][dy]:
                continue
            maps[dx][dy] = 0
            queue.append((dx, dy, step + 1))

    return -1