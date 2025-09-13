N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]
coin.sort(reverse=True)
cnt = 0
for c in coin:
    cnt += K // c
    K %= c
print(cnt)