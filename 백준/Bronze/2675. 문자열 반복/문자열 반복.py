T = int(input())
for i in range(T):
    R, S = input().split()
    ans = ''
    for alp in S:
        ans = ans + alp * int(R)
    print(ans)