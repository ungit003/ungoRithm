# 28235

# chant_dict = {
#     "SONGDO": "HIGHSCHOOL",
#     "CODE": "MASTER",
#     "2023": "0611",
#     "ALGORITHM": "CONTEST"
# }

# chant = input()
# print(chant_dict.get(chant, ""))

# 2446

# n = int(input())

# # 별 개수 감소하는 부분
# for i in range(n, 0, -1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# # 별 개수 증가하는 부분
# for i in range(2, n + 1):
#     print(" " * (n - i) + "*" * (2 * i - 1))

# 2991

A, B, C, D = map(int, input().split())
times = list(map(int, input().split()))  # P, M, N 도착 시간

for t in times:
    attacked = 0
    if 0 < t % (A + B) <= A:
        attacked += 1
    if 0 < t % (C + D) <= C:
        attacked += 1
    print(attacked)