l = []
t = 0
n = 0
answer = 0


def dfs(i, result):
    global l, t, n, answer

    if i == n:
        if result == t:
            answer += 1
        return
    else:
        dfs(i + 1, result + l[i])
        dfs(i + 1, result - l[i])


def solution(numbers, target):
    global l, t, n, answer

    l = numbers
    t = target
    n = len(numbers)

    dfs(0, 0)
    return answer


print(solution([1, 1, 1, 1, 1], 3))  # 5
print(solution([4, 1, 2, 1], 4))  # 2
