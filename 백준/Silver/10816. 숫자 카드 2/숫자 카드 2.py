N = int(input())
cards = list(map(int, input().split()))
M = int(input())
checks = list(map(int, input().split()))

check_dict = dict()
for check in checks:
    check_dict[check] = 0
# print(check_dict)

for card in cards:
    if card in check_dict:
        check_dict[card] += 1

# 이렇게 하면 출력 과정에서 순서가 바뀔 수 있음
# for value in check_dict.values():
#     print(value, end=' ')
for check in checks:
    print(check_dict[check], end=' ')