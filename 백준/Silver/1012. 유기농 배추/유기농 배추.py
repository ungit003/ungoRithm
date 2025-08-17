import sys
input = sys.stdin.readline
from collections import deque

def finder():
    idx = [(1,0),(0,1),(-1,0),(0,-1)]
    ans = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] != 1:
                continue
            queue = deque()
            queue.append((i, j))
            mat[i][j] = 2  # 시작점 방문 처리(중복 enqueue 방지)
            ans += 1
            while queue:
                i2, j2 = queue.popleft()
                for di, dj in idx:
                    i3, j3 = i2 + di, j2 + dj
                    if 0 <= i3 < N and 0 <= j3 < M and mat[i3][j3] == 1:
                        mat[i3][j3] = 2  # 발견 즉시 방문 처리
                        queue.append((i3, j3))
    return ans

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    mat = [[0]*M for _ in range(N)]
    for _ in range(K):
        x, y = map(int, input().split())
        mat[y][x] = 1
    print(finder())