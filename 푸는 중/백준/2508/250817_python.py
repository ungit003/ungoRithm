# 11726

# 시간초과
# def finder(n):
#     global ans
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     elif n >= 3:
#         return finder(n-1) + finder(n-2)
        
# n = int(input())
# ans = finder(n)
# print(ans % 10007)

# 파이파이가 더 메모리도 많이먹고 더 느린데 왜그럴까
# def finder(n):
#     ans_list = [0] * (n+1)
#     # print(ans_list)
#     ans_list[1] = 1
#     if n > 1:
#         ans_list[2] = 2
#     if n > 2:
#         for i in range(2, n):
#             # print(i)
#             ans_list[i+1] = ans_list[i] + ans_list[i-1]
#             # print(ans_list)
#     return ans_list[n]

# n = int(input())
# ans = finder(n)
# print(ans % 10007)


# 1012

# 시간 초과
# from collections import deque

# def finder():
#     # print('start')
#     idx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     ans = 0
#     for i in range(N):
#         for j in range(M):
#             if mat[i][j] == 0 or mat[i][j] == 2:
#                 # print(i, j, 'x')
#                 continue
#             # print(i, j, 'o')
#             queue = deque()
#             queue.append((i, j))
#             ans += 1
#             while queue:
#                 i2, j2 = queue.popleft()
#                 # print('queue', i2, j2)
#                 mat[i2][j2] += 1            
#                 for k in range(len(idx)):
#                     i3, j3 = i2 + idx[k][0], j2 + idx[k][1]
#                     # print('check', i3, j3)
#                     if 0 <= i3 < N and 0 <= j3 < M:
#                         if mat[i3][j3] == 0 or mat[i3][j3] == 2:
#                             # ('fail', i3, j3)
#                             continue
#                         queue.append((i3, j3))
#                         # print('add', i3, j3)
#     return ans

# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     mat = [[0] * M for _ in range(N)]
#     for _ in range(K):
#         x, y = map(int, input().split())
#         mat[y][x] = 1
#     # print(mat)

#     res = finder()
#     # print(mat)
#     print(res)

# import sys
# input = sys.stdin.readline
# from collections import deque

# def finder():
#     # print('start')
#     idx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
#     ans = 0
#     for i in range(N):
#         for j in range(M):
#             if mat[i][j] == 0 or mat[i][j] == 2:
#                 # print(i, j, 'x')
#                 continue
#             # print(i, j, 'o')
#             queue = deque()
#             queue.append((i, j))
#             ans += 1
#             while queue:
#                 i2, j2 = queue.popleft()
#                 # print('queue', i2, j2)
#                 mat[i2][j2] += 1            
#                 for k in range(len(idx)):
#                     i3, j3 = i2 + idx[k][0], j2 + idx[k][1]
#                     # print('check', i3, j3)
#                     if 0 <= i3 < N and 0 <= j3 < M:
#                         if mat[i3][j3] == 0 or mat[i3][j3] == 2:
#                             # ('fail', i3, j3)
#                             continue
#                         queue.append((i3, j3))
#                         # print('add', i3, j3)
#     return ans

# T = int(input())
# for _ in range(T):
#     M, N, K = map(int, input().split())
#     mat = [[0] * M for _ in range(N)]
#     for _ in range(K):
#         x, y = map(int, input().split())
#         mat[y][x] = 1
#     # print(mat)

#     res = finder()
#     # print(mat)
#     print(res)

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
