import sys
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
                S.add(x)