def make_impossible(mat, x, y):
    cnt_imp = 0
    for i in range(N):
        if mat[i][y] == 0:
            cnt_imp += 1
    for j in range(N):
        if mat[x][j] == 0:
            cnt_imp += 1
    




def finder(mat, n):
    if impossibles == N**2:
        if cnt != N:
            ans = 0
            return
        elif cnt == N:
            return
    
    for i in range(N):
        for j in range(N):
            if mat[N*i+j] == 0:

        


N = int(input())
possible = [0]*N*N
impossibles = 0
cnt = 0
ans = 0
finder(possible, 0)
print(ans)