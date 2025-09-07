# 7576

from collections import deque

def finder():
    res = 0
    cnt_m1 = 0
    cnt_p1 = 0
    queue = deque([])
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 1:
                queue.append((i, j, 0))
            elif mat[i][j] == -1:
                cnt_m1 += 1
    # print(queue, cnt_m1)
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    while queue:
        i, j, cnt = queue.popleft()
        cnt_p1 += 1
        if res != cnt:
            res += 1
        # print(i, j, cnt)
        for k in range(4):
            ni, nj = i + di[k], j + dj[k]
            if 0 <= ni < N and 0 <= nj < M:
                if mat[ni][nj] == 0:
                    queue.append((ni, nj, res+1))
                    mat[ni][nj] = 1
    if M * N != cnt_m1 + cnt_p1:
        res = -1
    return res

M, N = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

# print(mat)

ans = finder()
print(ans)

