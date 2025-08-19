import sys
input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

bot, top = 0, max((trees))
ans = 0

while bot <= top:
    mid = (bot + top) // 2
    cuts = 0
    for tree in trees:
        if tree > mid:
            cuts += tree - mid
        if cuts >= M:
            break

    if cuts >= M:
        ans = mid
        bot = mid + 1
    else:
        top = mid -1

print(ans)