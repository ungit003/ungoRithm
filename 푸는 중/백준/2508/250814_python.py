# 1003

# 시간초과
# def fibonacci_counter(num):
#     global cnt_0, cnt_1
#     if num == 0:
#         cnt_0 += 1
#         return
#     elif num == 1:
#         cnt_1 += 1
#         return
#     elif num >= 2:
#         fibonacci_counter(num-1)
#         fibonacci_counter(num-2)

# T = int(input())
# for _ in range(T):
#     test_num = int(input())
#     cnt_0, cnt_1 = 0, 0
#     fibonacci_counter(test_num)
#     print(cnt_0, cnt_1)


# def fibonacci_counter(num):
#     if num == 0:
#         print(1, 0)
#         return
#     # print('input:', num)
#     ans_list = [0] * (num+1)
#     ans_list[1] = 1
#     i = 1
#     while i < num:
#         ans_list[i+1] = ans_list[i] + ans_list[i-1]
#         i += 1
#     # print(ans_list)
#     print(ans_list[-2], ans_list[-1])

# T = int(input())
# for _ in range(T):
#     test_num = int(input())
#     fibonacci_counter(test_num)

# 1463

"""def finder(input, cnt):
    global min_cal
    if cnt > min_cal:
        return
    if input == 1:
        # print('ans:', input, cnt)
        ans_list.append(cnt)
        min_cal = cnt
        return
    if input % 3 == 0:
        # print('3:', input, cnt)
        finder(input // 3, cnt+1)
    if input % 2 == 0:
        # print('2:', input, cnt)
        finder(input // 2, cnt+1)
    # print('-:', input, cnt)
    finder(input - 1, cnt+1)

N = int(input())
min_cal = N
ans_list = []
finder(N, 0)
print(ans_list)
print(min(ans_list))"""

# def finder(input, cnt):
#     global min_cal
#     if cnt > min_cal:
#         return
#     if input == 1:
#         min_cal = cnt
#         return
#     if input % 3 == 0:
#         finder(input // 3, cnt+1)
#     if input % 2 == 0:
#         finder(input // 2, cnt+1)
#     finder(input - 1, cnt+1)

# N = int(input())
# min_cal = N
# finder(N, 0)
# print(min_cal)

# 2606

# 방문할 목록을 set으로 두고, visited가 true이면 제거하면서 순회를 시키는건 되나?
def finder(node):
    visited[node] = 1
    # print(node, edges[node])
    for i in range(1, N+1):
        if edges[node][i] == 0:
            continue
        if visited[i] == 1:
            continue
        finder(i)
    return

N = int(input())
M = int(input())
edges = [[0] * (N+1) for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    edges[a][b] = edges[b][a] = 1
# for edge in edges:
#     print(edge)

visited = [0] * (N+1)
finder(1)
# print(visited)
print(sum(visited)-1)