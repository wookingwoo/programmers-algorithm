def solution(s):
    stack = []

    for i in s:
        if i == "(":
            stack.append(i)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    if len(stack) == 0:
        return True
    else:
        return False


print(solution("()()"))  # True
print(solution("(())()"))  # True
print(solution(")()("))  # False
print(solution("(()("))  # False
