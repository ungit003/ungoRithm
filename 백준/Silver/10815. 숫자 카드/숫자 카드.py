N = int(input())
nums = set(map(int, input().split()))
M = int(input())
findings = list(map(int, input().split()))

for finding in findings:
    print(1 if finding in nums else 0, end=' ')