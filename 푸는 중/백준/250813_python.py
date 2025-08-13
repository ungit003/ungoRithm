# 11723

# 입력 저장했더니 메모리 초과
"""import sys
input = sys.stdin.readline

M = int(input())
orders = []
for _ in range(M):
    order = input().split()
    if len(order) == 2:
        order[1] = int(order[1])
    orders.append(order)
# print(orders)

S = set()
for order in orders:
    if len(order) == 2:
        ord, numb = order[0], order[1]
        if ord == 'add':
            if numb not in S:
                S.add(numb)
        elif ord == 'remove':
            if numb in S:
                S.remove(numb)
        elif ord == 'check':
            if numb in S:
                print(1)
            else:
                print(0)
        elif ord == 'toggle':
            if numb in S:
                S.remove(numb)
            else:
                S.add(numb)
    else:
        ord = order[0]
        if ord == 'all':
            S = set(range(1, 21))
        if ord == 'empty':
            S.clear()
# print(S)"""

# 입력 저장 안하고 바로 처리하면 답이 됨.
"""import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    parts = input().split()
    if len(parts) == 1:
        cmd = parts[0]
        if cmd == 'all':
            S = set(range(1, 21))  # 올바른 all 구현
        else:  # 'empty'
            S.clear()
    else:
        cmd, x = parts[0], int(parts[1])
        if cmd == 'add':
            S.add(x)
        elif cmd == 'remove':
            S.discard(x)  # remove 대신 discard
        elif cmd == 'check':
            print(1 if x in S else 0)
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)"""

# 1764

# 출력 양식을 잘 읽자
"""N, M = map(int, input().split())
users1 = set()
users2 = set()
for _ in range(N):
    users1.add(input())
for _ in range(M):
    users2.add(input())

users3 = sorted(users1.intersection(users2))
print(len(users3))
for user in users3:
    print(user)"""

# 11399

"""N = int(input())
times = sorted(map(int, input().split()), reverse=True)
print(times)

ans = 0
for i in range(N):
    ans += times[i] * (i+1)
print(ans)"""