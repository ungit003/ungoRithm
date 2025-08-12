N = int(input())
coors = []
for _ in range(N):
    x, y = map(int, input().split())
    coors.append((x, y))

coors.sort(key = lambda x: (x[0], x[1]))

for x, y in coors:
    print(x, y)