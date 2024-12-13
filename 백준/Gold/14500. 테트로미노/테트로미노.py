import sys
input = sys.stdin.readline

# 테트로미노의 모든 가능한 모양 정의
tetrominos = [
    [(0,0), (0,1), (0,2), (0,3)],
    [(0,0), (1,0), (2,0), (3,0)],
    [(0,0), (1,0), (0,1), (1,1)],
    [(0,0), (1,0), (2,0), (2,1)],
    [(0,1), (1,1), (2,1), (2,0)],
    [(0,0), (0,1), (1,1), (2,1)],
    [(0,0), (0,1), (1,0), (2,0)],
    [(0,0), (1,0), (1,1), (1,2)],
    [(0,2), (1,0), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,2)],
    [(0,0), (1,0), (0,1), (0,2)],
    [(0,0), (1,0), (1,1), (2,1)],
    [(0,1), (1,1), (1,0), (2,0)],
    [(0,1), (0,2), (1,0), (1,1)],
    [(0,0), (0,1), (1,1), (1,2)],
    [(0,0), (0,1), (0,2), (1,1)],
    [(0,1), (1,0), (1,1), (1,2)],
    [(0,0), (1,0), (1,1), (2,0)],
    [(0,1), (1,0), (1,1), (2,1)]
]

def calculate_max_sum(board, n, m):
    max_sum = 0
    for i in range(n):
        for j in range(m):
            for tetromino in tetrominos:
                current_sum = 0
                for dx, dy in tetromino:
                    nx, ny = i + dx, j + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        current_sum += board[nx][ny]
                    else:
                        break
                else:
                    max_sum = max(max_sum, current_sum)
    return max_sum

# 입력 받기
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 결과 계산 및 출력
result = calculate_max_sum(board, N, M)
print(result)
