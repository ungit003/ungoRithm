from collections import deque

def minimum_dice_throws(n, m, ladders, snakes):
    # 게임 보드 생성
    board = list(range(101))
    
    # 사다리와 뱀 배치
    for start, end in ladders + snakes:
        board[start] = end

    # BFS를 사용하여 100까지의 최단 경로 찾기
    queue = deque([(1, 0)])  # (현재_위치, 주사위_굴림_횟수)
    visited = [False] * 101
    visited[1] = True
    
    while queue:
        position, throws = queue.popleft()
        if position == 100:
            return throws

        for dice in range(1, 7):  # 주사위 결과 1부터 6까지
            next_position = position + dice
            if next_position <= 100 and not visited[next_position]:
                visited[next_position] = True
                next_position = board[next_position]  # 사다리나 뱀을 고려한 다음 위치
                queue.append((next_position, throws + 1))
    
    return -1  # 도달할 수 없는 경우 (입력이 올바르다면 이 경우는 없어야 함)

# 입력 받기
N, M = map(int, input().split())
ladders = [tuple(map(int, input().split())) for _ in range(N)]
snakes = [tuple(map(int, input().split())) for _ in range(M)]

# 결과 계산 및 출력
result = minimum_dice_throws(N, M, ladders, snakes)
print(result)