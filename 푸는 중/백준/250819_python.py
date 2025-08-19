# 2805

# 시간초과
# import sys
# input = sys.stdin.readline

# def finder():
#     ans = trees[0] - 1
#     # print(ans)
#     while True:
#         sum_cut = 0
#         for i in range(N):
#             cut = trees[i] - ans
#             if cut < 0:
#                 break
#             sum_cut += cut
#         # print(sum_cut)
#         if sum_cut >= M:
#             return ans
#         ans -= 1

# N, M = map(int, input().split())
# trees = sorted(map(int, input().split()), reverse=True)
# # print(trees)

# print((finder()))

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

bot, top = 0, max((trees))
ans = 0

while bot <= top:
    mid = (bot + top) // 2
    cuts = 0
    for tree in trees: 
        if tree > mid:
            cuts += tree - mid
        if cuts >= M:
            break

    if cuts >= M:
        ans = mid
        bot = mid + 1
    else:
        top = mid -1

print(ans)