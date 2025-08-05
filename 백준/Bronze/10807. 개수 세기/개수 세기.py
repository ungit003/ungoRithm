N = int(input())
nums = list(map(int, input().split()))
n = int(input())
ans = 0
for num in nums:
    if num == n:
        ans += 1
print(ans)