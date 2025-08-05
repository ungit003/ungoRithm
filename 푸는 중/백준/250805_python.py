# 10871

"""N, X = map(int, input().split())
nums = list(map(int, input().split()))
selected = list()
for num in nums:
    if num < X:
        selected.append(num)
print(selected)
for i in selected:
    print(i, end=' ')"""

# 10807

"""N = int(input())
nums = list(map(int, input().split()))
n = int(input())
ans = 0
for num in nums:
    if num == n:
        ans += 1
print(ans)"""

# 5597

"""students = list(range(1, 31))
subjects = list()
for i in range(28):
    subjects.append(int(input()))
for student in students:
    if student not in subjects:
        print(student)"""

# 2738

"""N, M = map(int, input().split())
mat1 = list()
mat2 = list()
for i in range(N):
    line = list(map(int, input().split()))
    mat1.append(line)
for i in range(N):
    line = list(map(int, input().split()))
    mat2.append(line)
print(mat1, mat2)
mat3 = list()
for i in range(N):
    line = list()
    for j in range(M):
        line.append(mat1[i][j] + mat2[i][j])
    mat3.append(line)
print(mat3)
for i in range(N):
    for j in range(M):
        print(mat3[i][j], end=" ")
    print()"""