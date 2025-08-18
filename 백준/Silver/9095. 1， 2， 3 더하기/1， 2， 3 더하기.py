def finder(n):
    global ans
    if n == 0:
        ans += 1
        return
    if n >= 1:
        # print(n, n-1)
        finder(n-1)
    if n >= 2:
        # print(n, n-2)
        finder(n-2)
    if n >= 3:
        # print(n, n-3)
        finder(n-3)
T = int(input())
for _ in range(T):
    n = int(input())
    ans = 0
    finder(n)
    print(ans)