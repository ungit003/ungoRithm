# 1330

"""A, B = map(int, input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')"""

# 9408

"""A = int(input())
if 90 <= A <= 100:
    print('A')
elif 80 <= A <= 89:
    print('B')
elif 70 <= A <= 79:
    print('C')
elif 60 <= A <= 69:
    print('D')
else:
    print('F')"""

# 14681

"""x = int(input())
y = int(input())
if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)"""

# 2753

"""A = int(input())
if A % 4 == 0:
    if A % 100 == 0:
        if A % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)"""

# 2420

"""N, M = map(int, input().split())
if (N >= 0 and M >= 0) or (N < 0 and M < 0):
    print(abs(N - M))
else:
    print(abs(N) + abs(M))"""

# 2741

"""A = int(input())
for i in range(A):
    print(i+1)"""

# 10872

"""A = int(input())
ans = 1
if A > 0:
    for i in range(A):
        ans = ans * (i+1)
print(ans)"""

# 10950

"""N = int(input())
for i in range(N):
    A, B = map(int, input().split())
    print(A + B)"""

# 10952

"""while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    else:
        print(A + B)"""

# 2739

"""N = int(input())
for i in range(9):
    print(N, "*", i+1, "=", N * (i+1))
for i in range(1, 10):
    print(f"{N} * {i} = {N*i}")"""

# 2438

"""n = int(input())
for i in range(n):
    print('*' * (i+1))"""

# 10951

"""while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break

import sys

for line in sys.stdin:
    a, b = map(int, line.split())
    print(a + b)"""

# 15552

n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(a + b)

import sys
input = sys.stdin.readline

N = int(input())
for _ in range(N):
    a, b = map(int, input().split())
    print(a + b)

