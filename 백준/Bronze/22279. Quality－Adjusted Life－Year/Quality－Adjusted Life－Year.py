n = int(input())
x = 0
for _ in range(n):
    a, b = map(float, input().split())
    x += a * b
print(f"{x:.2f}")