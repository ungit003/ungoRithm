import sys
sys.stdin = open("input.txt", "r")


def finder():
    if sum(arr[1:]) >= N * 2:
        return 0

    new_arr = [(max(arr[i] + i, i) - arr[i], i) for i in range(1, N + 1)]
    new_arr.sort(reverse=True)

    cnt = 0
    diff = N * 2 - sum(arr[1:])
    for val, idx in new_arr:
        if diff <= 0:
            break
        if val >= diff:
            cnt += 1
            break
        diff -= val
        cnt += 1
    return cnt

T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    ans = finder()
    print(f'#{tc+1} {ans}')