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