N, M = map(int, input().split())
money = N * 100
pay = M
if money >= pay:
    print('Yes')
else:
    print('No')