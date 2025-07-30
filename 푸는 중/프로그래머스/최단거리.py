import ast
from collections import deque

def finder():
    d = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 1)])
    
    while queue:
        x, y, step = queue.popleft()
        if x == 4 and y == 4:
            return step
        maps[x][y] = 0

        for elem in d:
            dx, dy = x + elem[0], y + elem[1]
            if not (0 <= dx < 5) or not (0 <= dy < 5):
                continue
            if not maps[dx][dy]:
                continue
            queue.append((dx, dy, step + 1))

    return -1

N = input()
'''
# 1. 대괄호 제거 및 공백 제거
N = N.strip()[2:-2]  # 양 끝의 대괄호 제거
print(N)

# 2. 쉼표를 기준으로 나누기
rows = N.split('],[')  # 각 행을 나눔
print(rows)

maps = []
for row in rows:
    # 3. 각 요소를 쉼표로 나누고, 숫자로 변환하여 리스트에 추가
    elements = row.split(',')
    maps.append([int(elem) for elem in elements])
'''
maps = ast.literal_eval(N)
print(finder())