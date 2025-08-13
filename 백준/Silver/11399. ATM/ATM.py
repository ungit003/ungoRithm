N = int(input())
times = sorted(map(int, input().split()), reverse=True)

ans = 0
for i in range(N):
    ans += times[i] * (i+1)
print(ans)