import sys
sys.stdin = open("input.txt", "r")


def finder():
    if sum(arr) >= N * 2:
        return 0

    new_arr = [0]
    for i in range(1, N + 1):
        new_arr.append(max(arr[i] + i, i))
    # print(new_arr)

    minus_arr = [-200001]
    for i in range(1, N + 1):
        minus_arr.append(new_arr[i] - arr[i])
    # print(minus_arr)

    sort_mi_arr = [(-200001, -200001, -200001)]
    for i in range(1, N + 1):
        sort_mi_arr.append((minus_arr[i], new_arr[i], i))
    sort_mi_arr.sort(reverse=True)
    # print(sort_mi_arr)

    cnt = 0
    while True:
        # print(sum(arr))
        if sum(arr) >= N * 2:
            break
        mns, value, idx = sort_mi_arr[cnt]
        arr[idx] = value
        cnt += 1
    return cnt


# 1.
T = int(input())
for tc in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().split()))
    # print(arr)
    # print(sum(arr))

    # 2.
    ans = finder()
    print(f'#{tc+1} {ans}')