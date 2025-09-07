# 15740

# import sys
# input = sys.stdin.readline

# A, B = map(int, input().split())
# print(A + B)

# 8370

# a, b, c, d = map(int, input().split())
# print(a*b + c*d)

# 15963

# a, b = map(int, input().split())
# if a == b:
#     print(1)
# else:
#     print(0)

# 15000

# a = input()
# print(a.upper())

# 24568

# a = int(input())
# b = int(input())
# ans = a*8 +b*3 -28
# if ans >= 0:
#     print(ans)
# else:
#     print(0)

# 28691

# d_dict = {'M':'MatKor', 'W':'WiCys', 'C':'CyKor', 'A':'AlKor', '$':'$clear'}
# a = input()
# print(d_dict[a])

# 10474

# while True:
#     a, b = map(int, input().split())
#     if a == b == 0:
#         break
#     print(a // b, a - a // b * b, '/', b)

# 15818

# n, m = map(int, input().split())
# nums = list(map(int, input().split()))
# ans = 1
# for i in range(n):
#     ans *= nums[i]
# print(ans % m)


# 1697

# 리커전에러
# def finder(now, time):
#     global max_time
#     if now == K:
#         if max_time > time:
#             max_time = time
#         return
#     if max_time > time:
#         if now + 1 <= 100000:
#             finder(now + 1, time+1)
#         if now - 1 >= 0:
#             finder(now - 1, time+1)
#         if now * 2 <= 100000:
#             finder(now * 2, time+1)
#     return

# N, K = map(int, input().split())
# max_time = abs(N - K)
# finder(N, 0)
# print(max_time)

# 리커전 에러
# def finder(now, time):
#     global max_time
#     visited[now] = 1
#     if now == K:
#         if max_time > time:
#             max_time = time
#         return
#     if max_time > time:
#         if now + 1 <= 100000 and visited[now + 1] == 0:
#             finder(now + 1, time+1)
#         if now - 1 >= 0 and visited[now - 1] == 0:
#             finder(now - 1, time+1)
#         if now * 2 <= 100000 and visited[now * 2] == 0:
#             finder(now * 2, time+1)
#     return

# N, K = map(int, input().split())
# max_time = abs(N - K)
# visited = [0] * 100001
# finder(N, 0)
# print(max_time)

# 비짓티드 안쓰니까 네임에러
# from collections import deque

# def finder(now):
#     visited = [0] * 100001
#     queue = deque([(now, 0)])

#     ans_time = abs(N - K)
#     while queue:
#         check, time = queue.popleft()
#         if check == K:
#             ans_time = time
#             break
#         visited[check] = 1
#         if check > 1 and visited[check-1] == 0:
#             queue.append((check-1, time+1))
#         if check < 99999 and visited[check+1] == 0:
#             queue.append((check+1, time+1))
#         if check <= 50000 and visited[check*2] == 0:
#             queue.append((check*2, time+1))
#     return ans_time

# N, K = map(int, input().split())
# print(finder(N))


# 14940

from collections import deque

def finder(i, j):
    # print('start')
    idx = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    queue = deque([(i, j, 0)])
    while queue:
        now_i, now_j, length = queue.popleft()
        # print(now_i, now_j, length)
        for di, dj in idx:
            new_i, new_j = now_i + di, now_j + dj
            if 0 <= new_i < n and 0 <= new_j < m:
                if land_info[new_i][new_j] == 1:
                    if ans_mat[new_i][new_j] == 0:
                        ans_mat[new_i][new_j] = length + 1
                        queue.append((new_i, new_j, length+1))
        # print(queue)

n, m = map(int, input().split())
land_info = []
for i in range(n):
    nums = list(map(int, input().split()))
    land_info.append(nums)

ans_mat = [[0] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if land_info[i][j] == 2:
            finder(i, j)
            ans_mat[i][j] = 0
for i in range(n):
    for j in range(m):
        if ans_mat[i][j] == 0 and land_info[i][j] == 1:
            ans_mat[i][j] = -1
for line in ans_mat:
    for elem in line:
        print(elem, end=' ')
    print()