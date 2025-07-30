from collections import deque
import copy


def finder():
    cnt_fuel = 16 * N * N
    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1

    queue = deque()
    queue.append((0, 0, 0, visited))

    d = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}

    while queue:
        fuel, x, y, visited = queue.popleft()
        if x == N-1 and y == N-1:
            cnt_fuel = min(cnt_fuel, fuel)
            continue
        for elem in d.values():
            dx, dy = x + elem[0], y + elem[1]
            if fuel > cnt_fuel:
                continue
            if not (0 <= dx < N) or not (0 <= dy < N):
                continue
            if visited[dx][dy]:
                continue
            if mat[x][y] > mat[dx][dy]:
                new_fuel = fuel
            elif mat[x][y] == mat[dx][dy]:
                new_fuel = fuel + 1
            elif mat[x][y] < mat[dx][dy]:
                new_fuel = fuel + (mat[dx][dy] - mat[x][y]) * 2
            new_visited = copy.deepcopy(visited)
            new_visited[dx][dy] = 1
            queue.append((new_fuel, dx, dy, new_visited))

    return cnt_fuel


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    ans = finder()
    print(f'#{tc+1} {ans}')