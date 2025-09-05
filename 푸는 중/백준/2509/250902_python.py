# 4714

while True:
    a = float(input())
    if a == -1:
        break
    print(f"Objects weighing {a:.2f} on Earth will weigh {a * 0.167:.2f} on the moon.")

# 12605

for i in range(int(input())):
    print(f"Case #{i + 1}: {' '.join(reversed(input().split()))}")