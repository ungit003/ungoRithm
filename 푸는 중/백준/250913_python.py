# 11047

# N, K = map(int, input().split())
# coin = [int(input()) for _ in range(N)]
# coin.sort(reverse=True)
# cnt = 0
# for c in coin:
#     cnt += K // c
#     K %= c
# print(cnt)

# 2630

def finder(start, end):
    if sum(map(sum, mat)) == 0:
        global white
        white += 1
        return
    elif sum(map(sum, mat)) == N * N:
        global blue
        blue += 1
        return
    

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
white = 0
blue = 0
finder(0, N)
print(white)
print(blue)

# 30979

# T = int(input())
# N = int(input())
# candy = list(map(int, input().split()))
# if sum(candy) < T:
#     print("Padaeng_i Cry")
# else:
#     print("Padaeng_i Happy")