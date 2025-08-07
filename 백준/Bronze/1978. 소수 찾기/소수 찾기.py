def isprime(x):
    if x == 1:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

N = int(input())
nums = list(map(int, input().split()))

ans = 0
for i in range(N):
    if isprime(nums[i]) == True:
        ans += 1
print(ans)