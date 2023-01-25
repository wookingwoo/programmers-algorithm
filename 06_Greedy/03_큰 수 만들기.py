# Level 2

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)

    if k > 0:
        stack = stack[:-k]

    return ''.join(stack)


print(solution("1924", 2))  # 94
print(solution("1231234", 3))  # 3234
print(solution("4177252841", 4))  # 775841
