from collections import deque

def finder():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque()
    queue.append((0, 0, 0, [0] * N * N))
    shortcut = 0
    for i in range(N):
        shortcut += mat[i][N - 1]
    for j in range(N):
        shortcut += mat[0][j]
    while queue:
        x, y, dist, visited = queue.popleft()
        if x == N-1 and y == N-1:
            shortcut = min(shortcut, dist)
        if dist > shortcut:
            continue
        visited[0] = 1
        for elem in d:
            dx, dy = x + elem[0], y + elem[1]
            if not ( 0 <= dx < N ) or not ( 0 <= dy < N ):
                continue
            if visited[dx * N + dy]:
                continue
            new_dist = dist + mat[dx][dy]
            new_visited = visited[:]
            new_visited[dx * N + dy] = 1
            queue.append((dx, dy, new_dist, new_visited))


    return shortcut


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, list(input()))) for _ in range(N)]
    
    print(finder())