# 11720

"""N = int(input())
nums = map(int, input())
print(sum(nums))"""

# 2562

"""num = 0
max_num = 0
for i in range(9):
    think = int(input())
    print("input", i, think)
    if think > max_num:
        num = i
        max_num = think
        print("output", num, max_num)
print(max_num)
print(num+1)"""

# 10818

"""N = int(input())
nums = list(map(int, input().split()))
nums.sort()
print(nums[0], nums[-1])"""

# 2675

"""T = int(input())
for i in range(T):
    R, S = input().split()
    ans = ''
    for alp in S:
        ans = ans + alp * int(R)
    print(ans)"""

# 4153

"""while True:
    a, b, c = map(int, input().split())
    if a == b == c == 0:
        break
    if (a*a + b*b == c*c) or (c*c + a*a == b*b) or (b*b + c*c == a*a):
        print('right')
    else:
        print('wrong')"""

# 30802

"""N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

tshirts = 0
for i in range(len(sizes)):
    if sizes[i] % T == 0:
        tshirts += sizes[i] // T 
    else:
        tshirts += sizes[i] // T + 1
print(tshirts)
print(N // P, N % P)"""