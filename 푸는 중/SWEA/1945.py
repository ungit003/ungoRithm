'''
숫자 N은 아래와 같다.

N=2^a x 3^b x 5^c x 7^d x 11^e
N이 주어질 때 a, b, c, d, e 를 출력하라.

[제약 사항]
N은 2 이상 10,000,000 이하이다.

[입력]
가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
각 테스트 케이스의 첫 번째 줄에 N 이 주어진다.

[출력]
출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
(t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)
'''
T = int(input())

for i in range(T) :
    N = int(input())
    alpha_list = {2: 0, 3: 0, 5: 0, 7: 0, 11: 0}
    for num in alpha_list.keys() :
        while True :
            if N % num == 0 :
                alpha_list[num] += 1 
                N = N // num
            else :
                break
    
    result = list(alpha_list.values())
    print(f'#{i+1} {result[0]} {result[1]} {result[2]} {result[3]} {result[4]}')