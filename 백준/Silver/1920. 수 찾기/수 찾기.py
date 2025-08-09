N = int(input())
nums = set(map(int, input().split()))
M = int(input())
findings = list(map(int, input().split()))

for target in findings:
    print(1 if target in nums else 0)