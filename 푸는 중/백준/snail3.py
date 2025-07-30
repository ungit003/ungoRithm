def finder(M, N):
    # m > n: 행이 열보다 큰 경우
    if M > N:
        turns = 2 * N - 1  # 꺾이는 횟수 계산
        if N % 2 == 0:
            # 열(n)이 짝수인 경우
            x, y = N // 2 + 1, N // 2
        else:
            # 열(n)이 홀수인 경우
            x, y = N // 2 + 1 + (M - N), N // 2 + 1

    # m < n: 행이 열보다 작은 경우
    elif M < N:
        turns = 2 * M - 2  # 꺾이는 횟수 계산
        if M % 2 == 0:
            # 행(m)이 짝수인 경우
            x, y = M // 2, M // 2
        else:
            # 행(m)이 홀수인 경우
            x, y = M // 2 + 1, M // 2 + 1 + (N - M)

    # m == n: 정사각형인 경우
    else:
        turns = 2 * N - 1  # 꺾이는 횟수 계산
        if N % 2 == 0:
            # 정사각형의 한 변(n)이 짝수인 경우
            x, y = N // 2 + 1, N // 2
        else:
            # 정사각형의 한 변(n)이 홀수인 경우
            x, y = N // 2 + 1, N // 2 + 1

    return turns, x, y

# 입력받기: 행(m)과 열(n)
m, n = map(int, input().split())

# 함수 호출하여 결과 계산
turns, x, y = finder(m, n)

# 결과 출력
print(turns)   # 꺾이는 횟수 출력
print(x, y)    # 달팽이가 멈추는 좌표 출력
