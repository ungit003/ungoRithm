from collections import deque


def finder(x, y):
    # 출발좌표 + 시간
    stt = (x, y, 1)
    visited = [[0] * M for _ in range(N)]
    # dir = {'U': (-1, 0), 'D': (1, 0), 'R': (0, 1), 'L':(0, -1)}
    dir_dict = {
        '1': [(0, 1), (1, 0), (0, -1), (-1, 0)],
        '2': [(1, 0), (-1, 0)],
        '3': [(0, 1), (0, -1)],
        '4': [(0, 1), (-1, 0)],
        '5': [(0, 1), (1, 0)],
        '6': [(1, 0), (0, -1)],
        '7': [(0, -1), (-1, 0)],
        }
    
    que = deque()
    que.append(stt)
    visited[x][y] = 1

    ans = 0
    time = 1
    while que:
        if time > L:
            break
        elem = que.popleft()
        print(elem)
        ans += 1
        if elem[2] < time:
            time += 1
            print('time + 1')

        num = mat[elem[0]][elem[1]]
        directions = dir_dict[num]

        for dir in directions:
            dx, dy = elem[0] + dir[0], elem[1] + dir[1]
            print(dx, dy)
            if 0 <= dx < N and 0 <= dy < M:
                if visited[dx][dy] == 0 and mat[dx][dy] != '0':
                    visited[dx][dy] = 1
                    que.append((dx, dy, time + 1))
            print(que)
            print(visited)
    return ans


T = int(input())
for tc in range(T):
    N, M, R, C, L = map(int, input().split())
    mat = [list(map(str, input().split())) for _ in range(N)]

    ans = finder(R, C)
    print(f'#{tc+1} {ans}')