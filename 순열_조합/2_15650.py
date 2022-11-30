# [BOJ] 15650 N과 M (2)

N, M = map(int, input().split())
nums = list(range(1, N+1))

result = []

def num():
    if len(result) == M:
        for i in result:
            print(i, end=' ')
        print()
    for i in nums:
        if len(result) == 0 or i > result[-1]:
            result.append(i)
            num()
            result.remove(i)

num()


def nums(a):
    if len(result) == M:
        print(*result)
    for i in range(a, N+1):
        result.append(i)
        nums(i+1)
        result.remove(i)

nums(1)