n = int(input())

# 별 개수 감소하는 부분
for i in range(n, 0, -1):
    print(" " * (n - i) + "*" * (2 * i - 1))

# 별 개수 증가하는 부분
for i in range(2, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))