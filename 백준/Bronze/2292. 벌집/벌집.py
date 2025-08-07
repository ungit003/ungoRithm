N = int(input())

ans = 1
while True:
    size = list(range(1, ans + 1))
    if sum(size) * 6 - ans * 6 + 1 >= N:
        break
    ans += 1

print(ans)