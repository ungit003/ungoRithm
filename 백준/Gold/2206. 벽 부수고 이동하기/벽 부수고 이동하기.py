from collections import deque

def bfs(matrix, n, m):
    # 방향 벡터 (상, 하, 좌, 우)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # 방문 여부를 저장하는 3차원 리스트 (행, 열, 벽 부숨 여부)
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    
    # 시작점 (x, y, 벽 부숨 여부, 거리)
    queue = deque([(0, 0, 0, 1)])  # (0, 0)에서 시작, 거리 1
    visited[0][0][0] = True  # (0, 0) 위치에서 벽을 부수지 않은 상태로 방문
    
    while queue:
        x, y, broke, dist = queue.popleft()
        
        # 도착점에 도달하면 거리 반환
        if x == n - 1 and y == m - 1:
            return dist
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:  # 범위 체크
                if matrix[nx][ny] == 0 and not visited[nx][ny][broke]:
                    # 이동할 칸이 비어있고, 아직 방문하지 않았다면
                    visited[nx][ny][broke] = True
                    queue.append((nx, ny, broke, dist + 1))
                elif matrix[nx][ny] == 1 and broke == 0 and not visited[nx][ny][1]:
                    # 이동할 칸이 벽이고, 아직 벽을 부수지 않았다면
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, 1, dist + 1))

    return -1  # 도착할 수 없는 경우

# 입력 처리
n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

# BFS 실행
result = bfs(matrix, n, m)
print(result)