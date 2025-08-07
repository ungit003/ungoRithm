N = int(input())
nums = list(map(int, input().split()))

ans = sum(nums) * 100 / max(nums) / N
print(ans)