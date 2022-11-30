#[BOJ] 15649 N과 M
"""
1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
각 수열은 공백으로 구분해서 출력
사전 순으로 증가하는 순서로 출력
5:38
"""

N, M = map(int, input().split())
nums = list(map(str, range(1, N+1)))


result = []


def num():
    if len(result) == M:
        print(' '.join(result))
        return
    for i in nums:
        if i not in result:
            result.append(i)
            num()
            result.remove(i)

num()


def nums(n, pre):
    if len(pre) == 2*M:
        print(pre.lstrip())
        return
    for i in range(1, N+1):
        if pre.find(str(i)) == -1:
            nums(n, f"{pre} {i}")



nums(N, "")