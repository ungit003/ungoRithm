def blackjack(list, number, sum):
    new_list = sorted(list)
    answer_list = []
    for i in range(number):
        for j in range(i+1, number):
            for k in range(j+1, number):
                if new_list[i] + new_list[j] + new_list[k] <= sum:
                    answer_list.append(new_list[i] + new_list[j] + new_list[k])
    answer_list.sort()
    return answer_list[-1]

N, M = map(int, input().split())
cards = list(map(int, input().split()))

print(blackjack(cards, N, M))