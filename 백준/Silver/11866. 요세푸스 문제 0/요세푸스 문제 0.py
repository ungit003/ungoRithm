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