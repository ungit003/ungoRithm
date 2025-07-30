def finder(i, j):
    global cnt_fuel, min_ans
    if i == N-1 and j == N-1:
        min_ans = min(cnt_fuel, min_ans)
        return
    d = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
    for elem in d.values():
        di, dj = i + elem[0], j + elem[1]
        if not (0 <= di < N) or not (0 <= dj < N):
            continue
        if visited[di][dj]:
            continue
        use_fuel = 0
        if mat[i][j] > mat[di][dj]:
            use_fuel = 0
        elif mat[i][j] == mat[di][dj]:
            use_fuel = 1
        elif mat[i][j] < mat[di][dj]:
            use_fuel = (mat[di][dj] - mat[i][j]) * 2
        visited[di][dj] = 1
        cnt_fuel += use_fuel
        finder(di, dj)
        cnt_fuel -= use_fuel
        visited[di][dj] = 0


T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    visited = [[0] * N for _ in range(N)]
    visited[0][0] = 1
    min_ans = 16 * N * N
    cnt_fuel = 0
    finder(0, 0)
    print(f'#{tc+1} {min_ans}')
