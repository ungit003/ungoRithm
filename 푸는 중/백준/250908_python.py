# 22279

n = int(input())
x = 0
for _ in range(n):
    a, b = map(float, input().split())
    x += a * b
print(f"{x:.2f}")

# 1284

while True:
    a = input()
    if a == "0":
        break
    cnt = 0
    for i in range(len(a)):
        if a[i] == "1":
            cnt += 2
        elif a[i] == "0":
            cnt += 4
        else:
            cnt += 3
    print(cnt + 2 + len(a) - 1)