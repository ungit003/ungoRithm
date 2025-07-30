T = int(input())
for tc in range(T):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    cal_mat = [[{} for _ in range(N)] for _ in range(N)]
    # for i in range(N):
    #     for j in range(N):
    print(cal_mat)
    for i in range(N):
        for j in range(N):

