# 2738

N, M = map(int, input().split())
mat1 = list()
mat2 = list()
for i in range(N):
    line = list(map(int, input().split()))
    mat1.append(line)
for i in range(N):
    line = list(map(int, input().split()))
    mat2.append(line)
mat3 = list()
for i in range(N):
    line = list()
    for j in range(M):
        line.append(mat1[i][j] + mat2[i][j])
    mat3.append(line)
for i in range(N):
    for j in range(M):
        print(mat3[i][j], end=" ")
    print()