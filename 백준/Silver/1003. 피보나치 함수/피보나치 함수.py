def fibonacci_counter(num):
    if num == 0:
        print(1, 0)
        return
    # print('input:', num)
    ans_list = [0] * (num+1)
    ans_list[1] = 1
    i = 1
    while i < num:
        ans_list[i+1] = ans_list[i] + ans_list[i-1]
        i += 1
    # print(ans_list)
    print(ans_list[-2], ans_list[-1])

T = int(input())
for _ in range(T):
    test_num = int(input())
    fibonacci_counter(test_num)