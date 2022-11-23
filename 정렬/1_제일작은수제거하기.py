# [Programmers] Level.1 제일 작은 수 제거하기

def solution(arr):
    arr.remove(min(arr))
    if len(arr) == 0:
        return [-1]
    return arr