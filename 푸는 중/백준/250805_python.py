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

# 11654

"""letter = input()
print(ord(letter))"""

# 2743

"""word = input()
print(word)
print(len(word))"""

# 2744

"""word = input()
print(word.swapcase())"""

# 2754

"""score = { 
'A+': 4.3, 'A0': 4.0, 'A-': 3.7,
'B+': 3.3, 'B0': 3.0, 'B-': 2.7,
'C+': 2.3, 'C0': 2.0, 'C-': 1.7,
'D+': 1.3, 'D0': 1.0, 'D-': 0.7,
'F': 0.0,
}

print(score[input()])"""

# 28766

"""S = input()
i = int(input())
print(S[i-1])"""

# 11718

"""while True:
    try:
        word = input()
        print(word)
    except EOFError:
        break"""

# 9086

"""T = int(input())
for i in range(T):
    word = input()
    print(word[0], word[-1], sep='')"""

# 15964

"""def new_cal(a, b):
    return (a + b) * (a - b) 

a, b = map(int, input().split())
print(new_cal(a, b))"""

# 2475

def cal(a, b, c, d, e):
    return (a*a + b*b + c*c + d*d + e*e) % 10

a, b, c, d, e = map(int, input().split())
print(cal(a, b, c, d, e))