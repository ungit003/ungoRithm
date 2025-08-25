A, B, C, D = map(int, input().split())
times = list(map(int, input().split()))  # P, M, N 도착 시간

for t in times:
    attacked = 0
    if 0 < t % (A + B) <= A:
        attacked += 1
    if 0 < t % (C + D) <= C:
        attacked += 1
    print(attacked)