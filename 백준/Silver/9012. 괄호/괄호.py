def check_VPS(string):
    ans = 'NO'
    if string[0] == ')':
        return print(ans)
    stack = ['(']
    for i in range(1, len(string)):
        if string[i] == '(':
            stack.append('(')
        else:
            if len(stack) == 0:
                return print(ans)
            elif stack[-1] == '(':
                stack.pop()
            elif stack[-1] == ')':
                stack.append(')')
    if len(stack) == 0:
        ans = 'YES'
    return print(ans)
    
T = int(input())
PS = []
for _ in range(T):
    PS.append(input())

for case in PS:
    check_VPS(case)