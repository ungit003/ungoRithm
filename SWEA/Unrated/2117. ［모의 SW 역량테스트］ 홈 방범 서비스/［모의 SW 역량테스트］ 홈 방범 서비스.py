def make_coordinate():
    coors = []
    K = 1
    while True:
        if K**2 +(K-1)**2 > M * cnt_1:
            break
        coor = []
        if K == 1:
            coor.append((0, 0))
        else:
            coor.extend(coors[-1])
            side = K-1
            for i in range(-side, side+1):
                for j in range(-side, side+1):
                    if abs(i) + abs(j) == side:
                        coor.append((i, j))            
        coors.append(coor)
        K += 1
    return coors


def finder(y, x):
    cnt = 0
    for i in range(len(c_mat)):
        cnt_h = 0
        for elem in c_mat[i]:
            dy, dx = y+elem[0], x+elem[1]
            if 0 <= dy < N and 0 <= dx < N:
                if mat[dy][dx] == 1:
                    cnt_h += 1
        if cnt < cnt_h and ((i+1)**2 + i**2 <= M * cnt_h):
            cnt = cnt_h
    return cnt


T = int(input())
for tc in range(T):
    N, M = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(N)]
    
    cnt_1 = sum([row.count(1) for row in mat])
    c_mat = make_coordinate()
    
    ans = 0
    for i in range(N):
        for j in range(N):
            res = finder(i, j)
            if res > ans:
                ans = res
    
    print(f'#{tc+1} {ans}')