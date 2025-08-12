def check_change(y, x):
    case1, case2 = 0, 0
    for i in range(y, y+8):
        for j in range(x, x+8):
            if i % 2 == 0:
                if rec[i][j] != ans1[j-x]:
                    case1 += 1
                if rec[i][j] != ans2[j-x]:
                    case2 += 1
            else:
                if rec[i][j] != ans2[j-x]:
                    case1 += 1
                if rec[i][j] != ans1[j-x]:
                    case2 += 1
    return min(case1, case2)

M, N = map(int, input().split())
rec = []
for _ in range(M):
    rec.append(input())

ans1, ans2 = '', ''
for i in range(8):
    if i % 2 == 0:
        ans1 += 'W'
        ans2 += 'B'
    else:
        ans1 += 'B'
        ans2 += 'W'

ans_list = []
for i in range(M-7):
    for j in range(N-7):
        ans_list.append(check_change(i, j))
print(min(ans_list))