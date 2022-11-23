# [Programmers] Level.1 예산

def solution(d, budget):
    answer = 0
    d.sort()
    sum = 0
    for i in range(len(d)):
        if (sum + d[i]) > budget:
            break
        sum += d[i]
        answer += 1
    return answer
