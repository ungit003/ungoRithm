#9095

# def finder(n):
#     global ans
#     if n == 0:
#         ans += 1
#         return
#     if n >= 1:
#         # print(n, n-1)
#         finder(n-1)
#     if n >= 2:
#         # print(n, n-2)
#         finder(n-2)
#     if n >= 3:
#         # print(n, n-3)
#         finder(n-3)
# T = int(input())
# for _ in range(T):
#     n = int(input())
#     ans = 0
#     finder(n)
#     print(ans)


# 11659

# from collections import deque

# 시간 초과
# def finder():
#     new_nums = nums
#     if i == j:
#         print(nums[i-1])
#     else:
#         p = 0
#         while True:
#             if p == i-1:
#                 break
#             new_nums.popleft()
#             p += 1
#         q = N-1
#         while True:
#             if q == j-1:
#                 break
#             new_nums.pop()
#             q -= 1
#         print(sum(new_nums))

# 메모리 초과
# N, M = map(int, input().split())
# nums = list(map(int, input().split()))

# sum_list = []
# line_list = []
# elem = 0
# for i in range(N):
#     elem += nums[i]
#     line_list.append(elem)
# sum_list.append(line_list)
# for i in range(N):
#     new_line = []
#     for j in range(N):
#         new_line.append(line_list[j] - line_list[i])
#     sum_list.append(new_line)
# # print(sum_list)

# for _ in range(M):
#     i, j = map(int, input().split())
#     # if i == 1:
#     #     print(line_list[j-1])
#     # else:
#     print(sum_list[i-1][j-1])

# 시간 초과
# import sys
# input = sys.stdin.readline

# N, M = map(int, input().split())
# nums = list(map(int, input().split()))
# for _ in range(M):
#     i, j = map(int, input().split())
#     ans = 0
#     for k in range(j-i):
#         ans += nums[i-1 + k]
#     print(ans)

# 임포트 바꾸기만 해도 속도가 엄청 빨라짐
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))

sums = [0]
elem = 0
for i in range(N):
    elem += nums[i]
    sums.append(elem)

# print(sums)

for _ in range(M):
    i, j = map(int, input().split())
    print(sums[j] - sums[i-1])