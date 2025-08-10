# 2439

# N = int(input())
# for i in range(1, N+1):
#     print(' '*(N-i), '*'*i, sep='')

# 11866

"""
1 2 3 4 5 6 7 -> 3 : 2
1 2 0 4 5 6 7 -> 6 : 5 == 2 + 3
1 2 0 4 5 0 7 -> 2 : 1 == 5 + 3 - 7
1 0 0 4 5 0 7 -> 5 : 4 == 1 + 3
1 0 0 4 0 0 7 -> 1 : 0 == 4 + 3 - 7
0 0 0 4

1 2 3 4 5 6 7 : 3 제거, 인덱스 : 2
1 2 4 5 6 7   : 6 제거, 인덱스 : 4 = 2 + 2
1 2 4 5 7     : 2 제거, 인덱스 : 1 = 4 + 2 - 5
1 4 5 7       : 7 제거, 인덱스 : 3 = 1 + 2
1 4 5         : 5 제거, 인덱스 : 2 = 3 + 2 - 3
1 4           : 1 제거, 인덱스 : 0 = 2 + 2 - 2 - 2
4             : 4 제거, 인덱스 : 0 


3 6 2 7 5 1 4
"""

N, K = map(int, input().split())

ans = []
people = list(range(1, N+1))
person_index = K-1
while True:
    # print(ans)
    if len(people) == 1:
        ans.append(people[0])
        break
    person = people.pop(person_index)
    ans.append(person)
    person_index += K-1
    while person_index >= len(people):
        # print(person_index, len(people))
        person_index -= len(people)
        # print(person_index, len(people))
print('<', end='')
print(', '.join(map(str, ans)), end='')
print('>')
"""
1 2 3 4 5 6 7
ans
[]
[3] 2 / 1 2 4 5 6 7
[3] 4 / 1 2 4 5 6 7
[3, 6] 4 / 1 2 4 5 7
[3, 6] 6 / 1 2 4 5 7
[3, 6] 1 / 1 2 4 5 7
[3, 6, 2] 1 / 1 4 5 7
[3, 6, 2] 3 / 1 4 5 7
[3, 6, 2, 7] 3 / 1 4 5
[3, 6, 2, 7] 5 / 1 4 5
[3, 6, 2, 7] 2 / 1 4 5
[3, 6, 2, 7, 5] 2 / 1 4
[3, 6, 2, 7, 5] 4 / 1 4
[3, 6, 2, 7, 5] 2 / 1 4
[3, 6, 2, 7, 5] 0 / 1 4
[3, 6, 2, 7, 5, 1] 0 / 4

"""